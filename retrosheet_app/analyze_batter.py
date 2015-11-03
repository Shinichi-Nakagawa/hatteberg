#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict
from retrosheet_util import RetroSheetUtil

__author__ = 'Shinichi Nakagawa'


class AnalyzeBatter(object):

    FIELD_POSITIONS_OF = OrderedDict([('7', 'LF'), ('8', 'CF'), ('9', 'RF')])
    FIELD_POSITIONS_IF = OrderedDict([('5', '3B'), ('6', 'SS'), ('4', '2B'), ('3', '1B')])
    FIELD_POSITIONS_BATTERY = OrderedDict([('2', 'C'), ('1', 'P')])
    HITS_DICT = {
        'HR': 'HR:Homerun',
        'T': '3B:Triple',
        'D': '2B:Double',
        'S': '1B:Single'
    }
    HITS = ('HR:Homerun', '3B:Triple', '2B:Double', '1B:Single')

    def __init__(self):
        pass

    def _initialize_hit_location_data(self, positions):
        """
        Initialize Hit Location Data
        :param positions: Position{'number': 'name'}
        :return: OrderedDict
        """
        hit_chart = OrderedDict()
        for pos in positions.keys():
            hits = OrderedDict()
            for hit in self.HITS:
                hits[hit] = 0
            hit_chart[positions[pos]] = hits
        return hit_chart

    @classmethod
    def _batted_ball_event(cls, batted_ball_event):
        """
        Batted ball event(Hits)
        :param batted_ball_event:
        :return: (str)Hits Event Text
        """
        _batted_ball_event = batted_ball_event
        if batted_ball_event == 'DGR':
            return 'D'
        return _batted_ball_event

    @classmethod
    def _batted_ball_position(cls, batted_ball_position):
        """
        Batted ball position
        :param batted_ball_position: Batted ball position by RETROSHEET
        :return: (str)position number(1-9)
        """
        _batted_ball_position = batted_ball_position
        if len(batted_ball_position) == 2:
            if batted_ball_position == '89':
                return '9'
            else:
                return _batted_ball_position[0:1]
        return _batted_ball_position

    def hit_location_data(
            self,
            df,
            pos_of=FIELD_POSITIONS_OF,
            pos_if=FIELD_POSITIONS_IF,
            pos_bt=FIELD_POSITIONS_BATTERY
    ):
        """
        Hit Location Data from RETROSHEET
        :param df: event file dataframe by RETROSHEET
        :param pos_of: Out Fielder Position{'number': 'name'}
        :param pos_if: In Fielder Position{'number': 'name'}
        :param pos_bt: BATTERY Position{'number': 'name'}
        :return:　Hit Location Data(dict)
        """
        hit_charts = {
            'of': self._initialize_hit_location_data(pos_of),
            'if': self._initialize_hit_location_data(pos_if),
            'battery': self._initialize_hit_location_data(pos_bt)
        }
        for i, row in df.iterrows():
            row_dict = row.to_dict()
            at_bat = RetroSheetUtil.get_atbat(
                row_dict['event_tx'],
                row_dict['event_cd'],
                row_dict['battedball_cd'],
            )
            batted_ball_event = AnalyzeBatter._batted_ball_event(at_bat['event'])
            batted_ball_pos = AnalyzeBatter._batted_ball_position(at_bat['position'])
            for k, pos in {'of': pos_of, 'if': pos_if, 'battery': pos_bt}.items():
                if batted_ball_pos in pos.keys():
                    hit_charts[k][pos[batted_ball_pos]][AnalyzeBatter.HITS_DICT[batted_ball_event]] += 1

        return hit_charts

    def _monthly_counts(
        self,
    ):
        return {m:0 for m in range(1,13)}

    def monthly_walks(
        self,
        walks,
    ):
        """
        Monthly Walks
        :param walks: atbat(walk) dataframe by RETROSHEET
        :return: Monthly Walk count(dict), Walk count(total)
        """
        ball_counts = 0
        monthly_counts = self._monthly_counts()
        for i, row in walks.iterrows():
            month = int(str(row['game_dt'])[4:6])
            monthly_counts[month] += 1
            ball_counts += 1
        return monthly_counts, ball_counts

    def monthly_walks_multi(
        self,
        walks,
    ):
        """
        Monthly Walks(マルチ散歩の回数)
        :param walks: atbat(walk) dataframe by RETROSHEET
        :return: Monthly Walk multi count(dict), Walk count(total)
        """
        ball_counts = 0
        monthly_counts = self._monthly_counts()
        multi_walks_counts = {}
        for i, row in walks.iterrows():
            month = int(str(row['game_dt'])[4:6])
            ball_counts += 1
            if row['game_id'] in multi_walks_counts:
                multi_walks_counts[row['game_id']] +=1
            else:
                multi_walks_counts[row['game_id']] =1
            if multi_walks_counts[row['game_id']] == 2:
                monthly_counts[month] += 1
        return monthly_counts, ball_counts

