#!/usr/bin/env python
# -*- coding: utf-8 -*-

from retrosheet_util import RetroSheetUtil
import unittest

__author__ = 'Shinichi Nakagawa'


class TestRetroSheetUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_first_strike(self):
        # ball
        self.assertFalse(RetroSheetUtil.is_first_strike('BBBB'))
        # strike
        self.assertTrue(RetroSheetUtil.is_first_strike('CFBBFBFC'))
        # 初球打ち
        self.assertTrue(RetroSheetUtil.is_first_strike('X'))
        # 初球牽制からのファール
        self.assertTrue(RetroSheetUtil.is_first_strike('1F1X'))
        # 初球牽制、二球目牽制からのボール
        self.assertFalse(RetroSheetUtil.is_first_strike('11BF1X'))

    def test_get_pitch_sequence(self):
        # walk
        self.assertEqual(
            RetroSheetUtil.get_pitch_sequence('BBBB', '14'),
            {
                'seq': [
                    'ball',
                    'ball',
                    'ball',
                    'ball',
                ],
                'ball': 4,
                'strike': 0,
                'pitches': 4,
                'pickoff': 0,
                'ball_count': {
                    'ball': 3,
                    'strike': 0,
                },
                'event': ('Walk',)
            }
        )
        # strike out
        self.assertEqual(
            RetroSheetUtil.get_pitch_sequence('CFBBFBFC', '3'),
            {
                'seq': [
                    'called strike',
                    'foul',
                    'ball',
                    'ball',
                    'foul',
                    'ball',
                    'foul',
                    'called strike',
                ],
                'ball': 3,
                'strike': 5,
                'pitches': 8,
                'pickoff': 0,
                'ball_count': {
                    'ball': 3,
                    'strike': 2,
                },
                'event': ('SO',)
            }
        )
        # single hit
        self.assertEqual(
            RetroSheetUtil.get_pitch_sequence('B1BCC>X', '20'),
            {
                'seq': [
                    'ball',
                    'pickoff throw to first',
                    'ball',
                    'called strike',
                    'called strike',
                    'indicates a runner going on the pitch',
                    'ball put into play by batter',
                ],
                'ball': 2,
                'strike': 2,
                'pitches': 5,
                'pickoff': 1,
                'ball_count': {
                    'ball': 2,
                    'strike': 2,
                },
                'event': ('S',)
            }
        )
        # intentional ball
        self.assertEqual(
            RetroSheetUtil.get_pitch_sequence('BFBBI', '15'),
            {
                'seq': [
                    'ball',
                    'foul',
                    'ball',
                    'ball',
                    'intentional ball'
                ],
                'ball': 4,
                'strike': 1,
                'pitches': 5,
                'pickoff': 0,
                'ball_count': {
                    'ball': 3,
                    'strike': 1,
                },
                'event': ('Intentional walk',)
            }
        )

    def test_get_atbat(self):

        # single
        self.assertEqual(
            RetroSheetUtil.get_atbat('S9/G.1-3', '20', 'G'),
            {'event': 'S', 'position': '9', 'battedball': 'G'}
        )

        # duble
        self.assertEqual(
            RetroSheetUtil.get_atbat('D57/G', 21, 'G'),
            {'event': 'D', 'position': '57', 'battedball': 'G'}
        )

        # ground rule duble
        self.assertEqual(
            RetroSheetUtil.get_atbat('DGR/9/F', '21', 'F'),
            {'event': 'DGR', 'position': '9', 'battedball': 'F'}
        )

        # ground rule duble(fan )
        self.assertEqual(
            RetroSheetUtil.get_atbat('DGR/FINT/7/L-.1-3', '21', 'L'),
            {'event': 'DGR', 'position': '7', 'battedball': 'L'}
        )

        # triple
        self.assertEqual(
            RetroSheetUtil.get_atbat('T9/L', '22', 'L'),
            {'event': 'T', 'position': '9', 'battedball': 'L'}
        )

        # home run
        self.assertEqual(
            RetroSheetUtil.get_atbat('HR/89/F.1-H', '23', 'F'),
            {'event': 'HR', 'position': '89', 'battedball': 'F'}
        )

        # home run(illegal position)
        self.assertEqual(
            RetroSheetUtil.get_atbat('HR/F8XD', '23', 'F'),
            {'event': 'HR', 'position': '8', 'battedball': 'F'}
        )

if __name__ == '__main__':
    unittest.main()
