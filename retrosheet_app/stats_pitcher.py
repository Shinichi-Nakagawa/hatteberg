#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from retrosheet_controller import RetroSheetDataController

__author__ = 'Shinichi Nakagawa'


class StatsPitcher(object):

    # 集計対象の年月
    FROM_YEAR = 2010
    TO_YEAR = 2014
    FROM_MONTH = 3
    TO_MONTH = 10

    def __init__(self):
        self.rs = RetroSheetDataController()

    def _read_games(self):
        return self.rs.read_sql_table('games')

    def win_of_month(self, player_id, from_year=FROM_YEAR, to_year=TO_YEAR, from_month=FROM_MONTH, to_month=TO_MONTH):
        """
        月ごとの勝利数
        :param player_id: 選手ID(Retrosheet)
        :param from_year: 開始年
        :param to_year: 終了年
        :param from_month: 開始月
        :param to_month: 終了月
        :return: DataFrame
        """
        games = self._read_games()
        return self._stats_of_month(games, player_id, from_year, to_year, from_month, to_month, games.WIN_PIT_ID)

    def lose_of_month(self, player_id, from_year=FROM_YEAR, to_year=TO_YEAR, from_month=FROM_MONTH, to_month=TO_MONTH):
        """
        月ごとの敗北数
        :param player_id: 選手ID(Retrosheet)
        :param from_year: 開始年
        :param to_year: 終了年
        :param from_month: 開始月
        :param to_month: 終了月
        :return: DataFrame
        """
        games = self._read_games()
        return self._stats_of_month(games, player_id, from_year, to_year, from_month, to_month, games.LOSE_PIT_ID)

    def _stats_of_month(self, games, player_id, from_year, to_year, from_month, to_month, search_column):
        """
        特定のStatsを月ごとに集計
        :param games: Dataframe for games table
        :param player_id: 選手ID(Retrosheet)
        :param from_year: 開始年
        :param to_year: 終了年
        :param from_month: 開始月
        :param to_month: 終了月
        :param search_column: 検索対象カラム
        :return: DataFrame
        """
        years = [y for y in range(from_year, to_year+1)]
        month_stats = []
        month = [m for m in range(from_month, to_month+1)]
        for mm in month:
            year_stats = []
            for yy in years:
                # 日付はInt型、月初月末の日付で絞る
                from_date = int('{yy}{mm:>02d}01'.format(yy=yy, mm=mm))
                to_date = int('{yy}{mm:>02d}31'.format(yy=yy, mm=mm))
                # 試合日(GAME_DT)のfrom/toで絞る
                df = games[
                    ((games.GAME_DT >= from_date) & (games.GAME_DT <= to_date))
                    &
                    (search_column == player_id)
                ]
                year_stats.append(len(df))
            month_stats.append(year_stats)
        return pd.DataFrame(np.array(month_stats), index=month, columns=years)


if __name__ == '__main__':
    p = StatsPitcher()
    win = p.win_of_month('lestj001')
