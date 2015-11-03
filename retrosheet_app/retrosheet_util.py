#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Shinichi Nakagawa'


class RetroSheetUtil(object):

    # at batとevent codeの対応表
    # http://www.retrosheet.org/datause.txt
    HITS_EVENT = {
        20: ('S',),
        21: ('DGR', 'D'),
        22: ('T',),
        23: ('HR',),
    }
    STRIKE_OUTS = {
        3: ('SO',),
    }
    OUTS = {
        2: ('OUTS',),
    }
    WALKS = {
        14: ('Walk',),
        15: ('Intentional walk',),

    }
    EVENT_TYPE = {
        k: v for event in (HITS_EVENT, STRIKE_OUTS, OUTS, WALKS) for k, v in event.items()
    }

    # Hitting event name
    ATBAT_NAMES = {
        'S': 'single',
        'D': 'double',
        'DGR': 'ground rule double',
        'T': 'triple',
        'HR': 'home run'
    }

    # pitching sequence
    # http://www.retrosheet.org/eventfile.htm

    # VS Batter
    PITCHING_SEQUENCE_VS_BATTER = {
        'B': 'ball',
        'C': 'called strike',
        'F': 'foul',
        'H': 'hit batter',
        'I': 'intentional ball',
        'K': 'strike (unknown type)',
        'L': 'foul bunt',
        'M': 'missed bunt attempt',
        'N': 'no pitch (on balks and interference calls)',
        'O': 'foul tip on bunt',
        'P': 'pitchout',
        'Q': 'swinging on pitchout',
        'R': 'foul ball on pitchout',
        'S': 'swinging strike',
        'T': 'foul tip',
        'U': 'unknown or missed pitch',
        'V': 'called ball because pitcher went to his mouth',
        'X': 'ball put into play by batter',
        'Y': 'ball put into play on pitchout',
    }

    # pickoff, catcher action(throw, blocked)
    PITCHING_SEQUENCE_EVENT = {
        '+': 'following pickoff throw by the catcher',
        '*': 'indicates the following pitch was blocked by the catcher',
        '.': 'marker for play not involving the batter',
        '1': 'pickoff throw to first',
        '2': 'pickoff throw to second',
        '3': 'pickoff throw to third',
        '>': 'indicates a runner going on the pitch',
    }

    PITCHING_SEQUENCE = {
        k: v for event in (PITCHING_SEQUENCE_VS_BATTER, PITCHING_SEQUENCE_EVENT) for k, v in event.items()
    }

    PITCHING_BALL = ('B', 'I')
    PITCHING_STRIKE = ('C', 'F', 'K', 'S', 'T')
    PITCHING_PICKOFF = ('1', '2', '3')
    PITCHING_BALL_IN_PLAY = ('X', 'Y')

    def __init__(self):
        pass

    @classmethod
    def parse_event_tx(cls, event_tx):
        """
        event text
        :param event_tx: event text by Retrosheet
        :return: event text list
        """
        _tx = event_tx
        return _tx.split('/')

    @classmethod
    def _ball_count(cls, ball, strike):
        """
        get ball count
        :param ball: (int)ball count
        :param strike: (int) strike count
        :return: ball & strike count(example)
        {
            'ball': 3,  # 0 <= ball <= 3
            'strike': 2, # 0 <= strike <= 2
        }
        """
        return {
            'ball': ball if ball <= 3 else 3,
            'strike': strike if strike <= 2 else 2,
        }

    @classmethod
    def is_first_strike(cls, pitch_tx):
        """
        初球がSTRIKEか否か
        :return: True(Strike) or False(Ball)
        """
        pitch_list = list(pitch_tx)
        for pitch in pitch_list:
            if pitch in RetroSheetUtil.PITCHING_SEQUENCE_EVENT.keys():
                continue
            if pitch in RetroSheetUtil.PITCHING_STRIKE:
                return True
            elif pitch in RetroSheetUtil.PITCHING_BALL_IN_PLAY:
                return True
            return False

    @classmethod
    def get_pitch_sequence(cls, pitch_tx, event_cd):
        """
        Pitching Sequence
        :param pitch_tx: pitching text by Retrosheet
        :param event_cd: event code by Retrosheet
        :return: pitchsequence text(example)
            {
                'seq': [
                    'ball',
                    'ball',
                    'foul',
                    'called strike',
                    'ball put into play by batter'
                ]
                'ball': 2
                'strike': 2,
                'pitches': 5,
                'pickoff': 0,
                'ball_count': {
                    'ball': 2,
                    'strike': 2,
                },
                'event': ('S')
            }
        """
        pitch_list = list(pitch_tx)
        pitch_seq = {
            'seq': [],
            'ball': 0,
            'strike': 0,
            'pitches': 0,
            'pickoff': 0,
            'ball_count': None,
            'event': None
        }
        for pitch in pitch_list:
            pitch_seq['seq'].append(RetroSheetUtil.PITCHING_SEQUENCE.get(pitch))
            if pitch in RetroSheetUtil.PITCHING_SEQUENCE_VS_BATTER:
                pitch_seq['pitches'] += 1
            if pitch in RetroSheetUtil.PITCHING_PICKOFF:
                pitch_seq['pickoff'] += 1
            if pitch in RetroSheetUtil.PITCHING_STRIKE:
                pitch_seq['strike'] += 1
            elif pitch in RetroSheetUtil.PITCHING_BALL:
                pitch_seq['ball'] += 1

        pitch_seq['event'] = RetroSheetUtil.EVENT_TYPE.get(int(event_cd),)
        pitch_seq['ball_count'] = RetroSheetUtil._ball_count(pitch_seq['ball'], pitch_seq['strike'])
        return pitch_seq

    @classmethod
    def get_atbat(cls, event_tx, event_cd, battedball_cd):
        """
        get at bat
        :param event_tx: event text by Retrosheet
        :param event_cd: event code by Retrosheet
        :param battedball_cd: battedball code by Retrosheet
        :return: batted ball(example)
            {
                'event': 'S'
                'position': '8',
                'battedball': 'linedrive',
            }
        """
        atbat = {
            'event': None,
            'position': None,
            'battedball': None
        }
        # イベントコードをみて、打球が飛んだ場合のみ処理(三振とか四球は無視)
        int_event_cd = int(event_cd)
        if int_event_cd not in cls.HITS_EVENT.keys():
            return atbat
        # event textをparse
        event_tx_list = cls.parse_event_tx(event_tx)
        for prefix in cls.HITS_EVENT.get(int_event_cd):
            if event_tx_list[0].startswith(prefix):
                atbat['event'] = prefix
                atbat['battedball'] = battedball_cd
                if prefix in ('HR', 'DGR'):
                    for event_tx_row in event_tx_list:
                        if event_tx_row.isdigit():
                            atbat['position'] = event_tx_row
                            return atbat
                    # positionがNoneの場合は最初にヒットした守備番号をpositionとする
                    if atbat['position'] is None:
                        for event_char in event_tx:
                            if event_char.isdigit():
                                atbat['position'] = event_char
                                return atbat
                            else:
                                continue
                else:
                    atbat['position'] = event_tx_list[0].replace(prefix, '')

                return atbat
