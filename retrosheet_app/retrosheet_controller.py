#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import select, and_, join
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from tables import t_rosters as rosters
from tables import Event, Game
from retrosheet_util import RetroSheetUtil

__author__ = 'Shinichi Nakagawa'


class RetroSheetDataController(object):

    FL_T = 't'
    DEFAULT_FROM_DT = '0101'
    DEFAULT_TO_DT = '1231'
    QUERY_SELECT_BATTING_STATS = """
    select
    g.game_dt,
    e.game_id, e.event_id, e.event_cd, e.pitch_seq_tx, e.event_tx, e.bat_play_tx, e.battedball_cd, e.battedball_loc_tx
    from games as g left outer join events as e on g.game_id = e.game_id
    """
    QUERY_SELECT_BATTING_STATS_WHERE = "where e.bat_id = '{bat_id}' and g.game_dt between {from_dt} and {to_dt}"
    QUERY_SELECT_BATTING_STATS_WHERE_EVENT_CODES = "and e.event_cd in({event_codes})"
    QUERY_SELECT_BATTING_STATS_WHERE_AT_BAT = "and e.ab_fl = '%s'" % (FL_T,)
    QUERY_SELECT_BATTING_STATS_ORDER_BY = "order by g.game_dt asc, e.event_id asc"
    QUERY_DATE_FORMAT = "{year}{dt}"
    QUERY_SELECT_BATTING_STATS_BY_EVENT_CODES = " ".join(
        [
            QUERY_SELECT_BATTING_STATS,
            QUERY_SELECT_BATTING_STATS_WHERE,
            QUERY_SELECT_BATTING_STATS_WHERE_EVENT_CODES,
            QUERY_SELECT_BATTING_STATS_ORDER_BY
        ]
    )
    QUERY_SELECT_BATTING_STATS_BY_AT_BAT = " ".join(
        [
            QUERY_SELECT_BATTING_STATS,
            QUERY_SELECT_BATTING_STATS_WHERE,
            QUERY_SELECT_BATTING_STATS_WHERE_AT_BAT,
            QUERY_SELECT_BATTING_STATS_ORDER_BY
        ]
    )

    def __init__(self, config_file='config.ini', database_engine='mysql'):
        config = ConfigParser()
        config.read(config_file)
        params = dict(config[database_engine])
        connection = "{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}".format(**params)
        encoding = params.get('encoding')
        self.engine = create_engine(connection, encoding=encoding)
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        self.conn = self.engine.connect()

    def _filter_by_event(self, first_name, last_name, year, from_dt, to_dt):
        """
        filter by event table
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: count
        """
        batter = self.get_player_data_one(year, first_name, last_name)
        return self.session.query(Event).select_from(join(Game, Event, Game.GAME_ID == Event.GAME_ID)).\
            filter(Event.BAT_ID == batter[rosters.c.PLAYER_ID.name]).\
            filter(
                Game.GAME_DT.between(
                    self.QUERY_DATE_FORMAT.format(year=year, dt=from_dt),
                    self.QUERY_DATE_FORMAT.format(year=year, dt=to_dt)
                )
            )

    def count_by_ab(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        AB count
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: ab(int)
        """
        return self._filter_by_event(first_name, last_name, year, from_dt, to_dt).\
            filter(Event.AB_FL == self.FL_T).\
            count()

    def count_by_pa(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        PA count
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: pa(int)
        """
        return self._filter_by_event(first_name, last_name, year, from_dt, to_dt).\
            filter(Event.BAT_EVENT_FL == self.FL_T).\
            count()

    def count_by_hits(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        Hits count
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: h(int)
        """
        return self._filter_by_event(first_name, last_name, year, from_dt, to_dt).\
            filter(Event.EVENT_CD.in_(RetroSheetUtil.HITS_EVENT.keys())).\
            count()

    def count_by_walk(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        Walk count
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: walk(int)
        """
        return self._filter_by_event(first_name, last_name, year, from_dt, to_dt).\
            filter(Event.EVENT_CD.in_(RetroSheetUtil.WALKS.keys())).\
            count()

    def count_by_so(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        Strike out count
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: so(int)
        """
        return self._filter_by_event(first_name, last_name, year, from_dt, to_dt).\
            filter(Event.EVENT_CD.in_(RetroSheetUtil.STRIKE_OUTS.keys())).\
            count()

    def count_by_event_cd(self, event_codes, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        event cd count
        :param event_codes: event code list by RETROSHEET
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: so(int)
        """
        return self._filter_by_event(first_name, last_name, year, from_dt, to_dt).\
            filter(Event.EVENT_CD.in_(event_codes)).\
            count()

    def _select_rosters_year_name(self, season_year, first_name, last_name):
        """
        select rosters where year & name
        :param season_year: Stats year
        :param first_name: First Name
        :param last_name: Last Name
        :return:
        """
        return select([rosters]).where(
            and_(
                rosters.c.YEAR == season_year,
                rosters.c.FIRST_NAME_TX == first_name,
                rosters.c.LAST_NAME_TX == last_name
            )
        )

    def get_player_data_one(self, season_year, first_name, last_name):
        """
        season毎の選手情報を取得
        :param season_year: Stats year
        :param first_name: First Name
        :param last_name: Last Name
        :return: (sqlalchemy.engine.result.RowProxy) Player Data
        """
        s = self._select_rosters_year_name(season_year, first_name, last_name)
        return self.conn.execute(s).fetchone()

    def read_sql_table(self, table_name):
        """
        指定したtableのデータフレームを返す
        :param table_name: table名
        :return: Dataframe
        """
        return pd.read_sql_table(table_name=table_name, con=self.engine)

    def read_sql_query(self, query):
        """
        検索条件を元にデータフレームを返す
        :param query: 検索条件
        :return: Dataframe
        """
        return pd.read_sql_query(sql=query, con=self.engine)

    def batter_event_by_at_bat(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        get batter at bat result
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: Dataframe
        """
        batter = self.get_player_data_one(year, first_name, last_name)
        params = self._batter_event_query_params(batter, year, from_dt, to_dt)
        return self.read_sql_query(self.QUERY_SELECT_BATTING_STATS_BY_AT_BAT.format(**params))

    def batter_event_by_so(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        get batter strike outs result
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: Dataframe
        """
        event_codes = (str(cd) for cd in RetroSheetUtil.STRIKE_OUTS.keys())
        return self._batter_event_query(first_name, last_name, year, from_dt, to_dt, event_codes)

    def batter_event_by_walk(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        get batter walk result
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: Dataframe
        """
        event_codes = (str(cd) for cd in RetroSheetUtil.WALKS.keys())
        return self._batter_event_query(first_name, last_name, year, from_dt, to_dt, event_codes)

    def batter_event_by_hits(self, first_name, last_name, year, from_dt=DEFAULT_FROM_DT, to_dt=DEFAULT_TO_DT):
        """
        get batter hits result
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: Dataframe
        """
        event_codes = (str(cd) for cd in RetroSheetUtil.HITS_EVENT.keys())
        return self._batter_event_query(first_name, last_name, year, from_dt, to_dt, event_codes)

    def _batter_event_query(self, first_name, last_name, year, from_dt, to_dt, event_codes):
        """
        batting result(event)
        :param first_name: batter first name
        :param last_name: batter last name
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :param event_codes: Event List
        :return: Dataframe
        """
        batter = self.get_player_data_one(year, first_name, last_name)
        params = self._batter_event_query_params(batter, year, from_dt, to_dt)
        params['event_codes'] = ",".join(event_codes)
        return self.read_sql_query(self.QUERY_SELECT_BATTING_STATS_BY_EVENT_CODES.format(**params))

    def _batter_event_query_params(self, batter, year, from_dt, to_dt):
        """
        batting result
        :param batter: batter model
        :param year: season year
        :param from_dt: from date
        :param to_dt: to date
        :return: dictionary
        """
        return {
            'bat_id': batter[rosters.c.PLAYER_ID.name],
            'from_dt': self.QUERY_DATE_FORMAT.format(year=year, dt=from_dt),
            'to_dt': self.QUERY_DATE_FORMAT.format(year=year, dt=to_dt),
        }


if __name__ == '__main__':
    rs = RetroSheetDataController()
