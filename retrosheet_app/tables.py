# coding: utf-8
from sqlalchemy import Column, Index, Integer, String, Table, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_LKUP_CD_BASES = Table(
    'LKUP_CD_BASES', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_BATTEDBALL = Table(
    'LKUP_CD_BATTEDBALL', metadata,
    Column('VALUE_CD', String(1)),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_EVENT = Table(
    'LKUP_CD_EVENT', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_FLD = Table(
    'LKUP_CD_FLD', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_H = Table(
    'LKUP_CD_H', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_HAND = Table(
    'LKUP_CD_HAND', metadata,
    Column('VALUE_CD', String(1)),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_PARK_DAYNIGHT = Table(
    'LKUP_CD_PARK_DAYNIGHT', metadata,
    Column('VALUE_CD', String(1)),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_PARK_FIELD = Table(
    'LKUP_CD_PARK_FIELD', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_PARK_PRECIP = Table(
    'LKUP_CD_PARK_PRECIP', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_PARK_SKY = Table(
    'LKUP_CD_PARK_SKY', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_PARK_WIND_DIRECTION = Table(
    'LKUP_CD_PARK_WIND_DIRECTION', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_RECORDER_METHOD = Table(
    'LKUP_CD_RECORDER_METHOD', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_CD_RECORDER_PITCHES = Table(
    'LKUP_CD_RECORDER_PITCHES', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_ID_BASE = Table(
    'LKUP_ID_BASE', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_ID_HOME = Table(
    'LKUP_ID_HOME', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


t_LKUP_ID_LAST = Table(
    'LKUP_ID_LAST', metadata,
    Column('VALUE_CD', Integer),
    Column('SHORTNAME_TX', String(8)),
    Column('LONGNAME_TX', String(30)),
    Column('DESCRIPTION_TX', String(255))
)


class Event(Base):
    __tablename__ = 'events'
    __table_args__ = (
        Index('index_resp_pit_id', 'RESP_PIT_ID', 'GAME_ID'),
        Index('index_pos2_fld_id', 'POS2_FLD_ID', 'GAME_ID'),
        Index('index_pos3_fld_id', 'POS3_FLD_ID', 'GAME_ID'),
        Index('index_pos4_fld_id', 'POS4_FLD_ID', 'GAME_ID'),
        Index('index_pos5_fld_id', 'POS5_FLD_ID', 'GAME_ID'),
        Index('index_pos6_fld_id', 'POS6_FLD_ID', 'GAME_ID'),
        Index('index_pos7_fld_id', 'POS7_FLD_ID', 'GAME_ID'),
        Index('index_pos8_fld_id', 'POS8_FLD_ID', 'GAME_ID'),
        Index('index_pos9_fld_id', 'POS9_FLD_ID', 'GAME_ID'),
        Index('index_base1_run_id', 'BASE1_RUN_ID', 'GAME_ID'),
        Index('index_base2_run_id', 'BASE2_RUN_ID', 'GAME_ID'),
        Index('index_base3_run_id', 'BASE3_RUN_ID', 'GAME_ID'),
        Index('index_run1_resp_pit_id', 'RUN1_RESP_PIT_ID', 'GAME_ID'),
        Index('index_run2_resp_pit_id', 'RUN2_RESP_PIT_ID', 'GAME_ID'),
        Index('index_run3_resp_pit_id', 'RUN3_RESP_PIT_ID', 'GAME_ID'),
        Index('index_removed_for_pr_run1_id', 'REMOVED_FOR_PR_RUN1_ID', 'GAME_ID'),
        Index('index_removed_for_pr_run2_id', 'REMOVED_FOR_PR_RUN2_ID', 'GAME_ID'),
        Index('index_removed_for_pr_run3_id', 'REMOVED_FOR_PR_RUN3_ID', 'GAME_ID'),
        Index('index_removed_for_ph_bat_id', 'REMOVED_FOR_PH_BAT_ID', 'GAME_ID'),
        Index('index_run1_resp_cat_id', 'RUN1_RESP_CAT_ID', 'GAME_ID'),
        Index('index_run2_resp_cat_id', 'RUN2_RESP_CAT_ID', 'GAME_ID'),
        Index('index_run3_resp_cat_id', 'RUN3_RESP_CAT_ID', 'GAME_ID'),
        Index('index_bat_id', 'BAT_ID', 'GAME_ID'),
        Index('index_pit_id', 'PIT_ID', 'GAME_ID'),
        Index('index_resp_bat_id', 'RESP_BAT_ID', 'GAME_ID'),
        Index('index_bat_on_deck_id', 'BAT_ON_DECK_ID', 'GAME_ID'),
        Index('index_bat_in_hold_id', 'BAT_IN_HOLD_ID', 'GAME_ID')
    )

    GAME_ID = Column(String(12), primary_key=True, nullable=False, server_default=text("''"))
    AWAY_TEAM_ID = Column(String(3))
    INN_CT = Column(Integer)
    BAT_HOME_ID = Column(Integer)
    OUTS_CT = Column(Integer)
    BALLS_CT = Column(Integer)
    STRIKES_CT = Column(Integer)
    PITCH_SEQ_TX = Column(String(40))
    AWAY_SCORE_CT = Column(Integer)
    HOME_SCORE_CT = Column(Integer)
    BAT_ID = Column(String(8))
    BAT_HAND_CD = Column(String(1))
    RESP_BAT_ID = Column(String(8))
    BAT_ON_DECK_ID = Column(String(8))
    BAT_IN_HOLD_ID = Column(String(8))
    RESP_BAT_HAND_CD = Column(String(1))
    PIT_ID = Column(String(8))
    PIT_HAND_CD = Column(String(1))
    RESP_PIT_ID = Column(String(8))
    RESP_PIT_HAND_CD = Column(String(1))
    POS2_FLD_ID = Column(String(8))
    POS3_FLD_ID = Column(String(8))
    POS4_FLD_ID = Column(String(8))
    POS5_FLD_ID = Column(String(8))
    POS6_FLD_ID = Column(String(8))
    POS7_FLD_ID = Column(String(8))
    POS8_FLD_ID = Column(String(8))
    POS9_FLD_ID = Column(String(8))
    BASE1_RUN_ID = Column(String(8))
    BASE2_RUN_ID = Column(String(8))
    BASE3_RUN_ID = Column(String(8))
    EVENT_TX = Column(String(100))
    LEADOFF_FL = Column(String(1))
    PH_FL = Column(String(1))
    BAT_FLD_CD = Column(Integer)
    BAT_LINEUP_ID = Column(Integer)
    EVENT_CD = Column(Integer)
    BAT_EVENT_FL = Column(String(1))
    AB_FL = Column(String(1))
    H_CD = Column(Integer)
    SH_FL = Column(String(1))
    SF_FL = Column(String(1))
    EVENT_OUTS_CT = Column(Integer)
    DP_FL = Column(String(1))
    TP_FL = Column(String(1))
    RBI_CT = Column(Integer)
    WP_FL = Column(String(1))
    PB_FL = Column(String(1))
    FLD_CD = Column(Integer)
    BATTEDBALL_CD = Column(String(1))
    BUNT_FL = Column(String(1))
    FOUL_FL = Column(String(1))
    BATTEDBALL_LOC_TX = Column(String(5))
    ERR_CT = Column(Integer)
    ERR1_FLD_CD = Column(Integer)
    ERR1_CD = Column(String(1))
    ERR2_FLD_CD = Column(Integer)
    ERR2_CD = Column(String(1))
    ERR3_FLD_CD = Column(Integer)
    ERR3_CD = Column(String(1))
    BAT_DEST_ID = Column(Integer)
    RUN1_DEST_ID = Column(Integer)
    RUN2_DEST_ID = Column(Integer)
    RUN3_DEST_ID = Column(Integer)
    BAT_PLAY_TX = Column(String(8))
    RUN1_PLAY_TX = Column(String(15))
    RUN2_PLAY_TX = Column(String(15))
    RUN3_PLAY_TX = Column(String(15))
    RUN1_SB_FL = Column(String(1))
    RUN2_SB_FL = Column(String(1))
    RUN3_SB_FL = Column(String(1))
    RUN1_CS_FL = Column(String(1))
    RUN2_CS_FL = Column(String(1))
    RUN3_CS_FL = Column(String(1))
    RUN1_PK_FL = Column(String(1))
    RUN2_PK_FL = Column(String(1))
    RUN3_PK_FL = Column(String(1))
    RUN1_RESP_PIT_ID = Column(String(8))
    RUN2_RESP_PIT_ID = Column(String(8))
    RUN3_RESP_PIT_ID = Column(String(8))
    GAME_NEW_FL = Column(String(1))
    GAME_END_FL = Column(String(1))
    PR_RUN1_FL = Column(String(1))
    PR_RUN2_FL = Column(String(1))
    PR_RUN3_FL = Column(String(1))
    REMOVED_FOR_PR_RUN1_ID = Column(String(8))
    REMOVED_FOR_PR_RUN2_ID = Column(String(8))
    REMOVED_FOR_PR_RUN3_ID = Column(String(8))
    REMOVED_FOR_PH_BAT_ID = Column(String(8))
    REMOVED_FOR_PH_BAT_FLD_CD = Column(Integer)
    PO1_FLD_CD = Column(Integer)
    PO2_FLD_CD = Column(Integer)
    PO3_FLD_CD = Column(Integer)
    ASS1_FLD_CD = Column(Integer)
    ASS2_FLD_CD = Column(Integer)
    ASS3_FLD_CD = Column(Integer)
    ASS4_FLD_CD = Column(Integer)
    ASS5_FLD_CD = Column(Integer)
    EVENT_ID = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    HOME_TEAM_ID = Column(String(3))
    BAT_TEAM_ID = Column(String(3))
    FLD_TEAM_ID = Column(String(3))
    BAT_LAST_ID = Column(Integer)
    INN_NEW_FL = Column(String(1))
    INN_END_FL = Column(String(1))
    START_BAT_SCORE_CT = Column(Integer)
    START_FLD_SCORE_CT = Column(Integer)
    INN_RUNS_CT = Column(Integer)
    GAME_PA_CT = Column(Integer)
    INN_PA_CT = Column(Integer)
    PA_NEW_FL = Column(String(1))
    PA_TRUNC_FL = Column(String(1))
    START_BASES_CD = Column(Integer)
    END_BASES_CD = Column(Integer)
    BAT_START_FL = Column(String(1))
    RESP_BAT_START_FL = Column(String(1))
    PIT_START_FL = Column(String(1))
    RESP_PIT_START_FL = Column(String(1))
    RUN1_FLD_CD = Column(Integer)
    RUN1_LINEUP_CD = Column(Integer)
    RUN1_ORIGIN_EVENT_ID = Column(Integer)
    RUN2_FLD_CD = Column(Integer)
    RUN2_LINEUP_CD = Column(Integer)
    RUN2_ORIGIN_EVENT_ID = Column(Integer)
    RUN3_FLD_CD = Column(Integer)
    RUN3_LINEUP_CD = Column(Integer)
    RUN3_ORIGIN_EVENT_ID = Column(Integer)
    RUN1_RESP_CAT_ID = Column(String(8))
    RUN2_RESP_CAT_ID = Column(String(8))
    RUN3_RESP_CAT_ID = Column(String(8))
    PA_BALL_CT = Column(Integer)
    PA_CALLED_BALL_CT = Column(Integer, server_default=text("'0'"))
    PA_INTENT_BALL_CT = Column(Integer)
    PA_PITCHOUT_BALL_CT = Column(Integer)
    PA_HITBATTER_BALL_CT = Column(Integer)
    PA_OTHER_BALL_CT = Column(Integer)
    PA_STRIKE_CT = Column(Integer)
    PA_CALLED_STRIKE_CT = Column(Integer)
    PA_SWINGMISS_STRIKE_CT = Column(Integer)
    PA_FOUL_STRIKE_CT = Column(Integer)
    PA_INPLAY_STRIKE_CT = Column(Integer)
    PA_OTHER_STRIKE_CT = Column(Integer)
    EVENT_RUNS_CT = Column(Integer)
    FLD_ID = Column(String(8))
    BASE2_FORCE_FL = Column(String(1))
    BASE3_FORCE_FL = Column(String(1))
    BASE4_FORCE_FL = Column(String(1))
    BAT_SAFE_ERR_FL = Column(String(1))
    BAT_FATE_ID = Column(Integer)
    RUN1_FATE_ID = Column(Integer)
    RUN2_FATE_ID = Column(Integer)
    RUN3_FATE_ID = Column(Integer)
    FATE_RUNS_CT = Column(Integer)
    ASS6_FLD_CD = Column(Integer)
    ASS7_FLD_CD = Column(Integer)
    ASS8_FLD_CD = Column(Integer)
    ASS9_FLD_CD = Column(Integer)
    ASS10_FLD_CD = Column(Integer)
    UNKNOWN_OUT_EXC_FL = Column(String(1))
    UNCERTAIN_PLAY_EXC_FL = Column(String(1))


class Game(Base):
    __tablename__ = 'games'
    __table_args__ = (
        Index('index_win_pit_id', 'WIN_PIT_ID', 'GAME_DT'),
        Index('index_lose_pit_id', 'LOSE_PIT_ID', 'GAME_DT'),
        Index('index_save_pit_id', 'SAVE_PIT_ID', 'GAME_DT'),
        Index('index_gwrbi_bat_id', 'GWRBI_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup1_bat_id', 'AWAY_LINEUP1_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup2_bat_id', 'AWAY_LINEUP2_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup3_bat_id', 'AWAY_LINEUP3_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup4_bat_id', 'AWAY_LINEUP4_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup5_bat_id', 'AWAY_LINEUP5_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup6_bat_id', 'AWAY_LINEUP6_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup7_bat_id', 'AWAY_LINEUP7_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup8_bat_id', 'AWAY_LINEUP8_BAT_ID', 'GAME_DT'),
        Index('index_away_lineup9_bat_id', 'AWAY_LINEUP9_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup1_bat_id', 'HOME_LINEUP1_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup2_bat_id', 'HOME_LINEUP2_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup3_bat_id', 'HOME_LINEUP3_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup4_bat_id', 'HOME_LINEUP4_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup5_bat_id', 'HOME_LINEUP5_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup6_bat_id', 'HOME_LINEUP6_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup7_bat_id', 'HOME_LINEUP7_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup8_bat_id', 'HOME_LINEUP8_BAT_ID', 'GAME_DT'),
        Index('index_home_lineup9_bat_id', 'HOME_LINEUP9_BAT_ID', 'GAME_DT'),
        Index('index_away_finish_pit_id', 'AWAY_FINISH_PIT_ID', 'GAME_DT'),
        Index('index_home_finish_pit_id', 'HOME_FINISH_PIT_ID', 'GAME_DT')
    )

    GAME_ID = Column(String(12), primary_key=True)
    GAME_DT = Column(Integer, index=True)
    GAME_CT = Column(Integer)
    GAME_DY = Column(String(9))
    START_GAME_TM = Column(Integer)
    DH_FL = Column(String(1))
    DAYNIGHT_PARK_CD = Column(String(1))
    AWAY_TEAM_ID = Column(String(3))
    HOME_TEAM_ID = Column(String(3))
    PARK_ID = Column(String(5))
    AWAY_START_PIT_ID = Column(String(8))
    HOME_START_PIT_ID = Column(String(8))
    BASE4_UMP_ID = Column(String(8))
    BASE1_UMP_ID = Column(String(8))
    BASE2_UMP_ID = Column(String(8))
    BASE3_UMP_ID = Column(String(8))
    LF_UMP_ID = Column(String(8))
    RF_UMP_ID = Column(String(8))
    ATTEND_PARK_CT = Column(Integer)
    SCORER_RECORD_ID = Column(String(50))
    TRANSLATOR_RECORD_ID = Column(String(50))
    INPUTTER_RECORD_ID = Column(String(50))
    INPUT_RECORD_TS = Column(String(18))
    EDIT_RECORD_TS = Column(String(18))
    METHOD_RECORD_CD = Column(String(18))
    PITCHES_RECORD_CD = Column(String(1))
    TEMP_PARK_CT = Column(Integer)
    WIND_DIRECTION_PARK_CD = Column(Integer)
    WIND_SPEED_PARK_CT = Column(Integer)
    FIELD_PARK_CD = Column(Integer)
    PRECIP_PARK_CD = Column(Integer)
    SKY_PARK_CD = Column(Integer)
    MINUTES_GAME_CT = Column(Integer)
    INN_CT = Column(Integer)
    AWAY_SCORE_CT = Column(Integer)
    HOME_SCORE_CT = Column(Integer)
    AWAY_HITS_CT = Column(Integer)
    HOME_HITS_CT = Column(Integer)
    AWAY_ERR_CT = Column(Integer)
    HOME_ERR_CT = Column(Integer)
    AWAY_LOB_CT = Column(Integer)
    HOME_LOB_CT = Column(Integer)
    WIN_PIT_ID = Column(String(8))
    LOSE_PIT_ID = Column(String(8))
    SAVE_PIT_ID = Column(String(8))
    GWRBI_BAT_ID = Column(String(8))
    AWAY_LINEUP1_BAT_ID = Column(String(8))
    AWAY_LINEUP1_FLD_CD = Column(Integer)
    AWAY_LINEUP2_BAT_ID = Column(String(8))
    AWAY_LINEUP2_FLD_CD = Column(Integer)
    AWAY_LINEUP3_BAT_ID = Column(String(8))
    AWAY_LINEUP3_FLD_CD = Column(Integer)
    AWAY_LINEUP4_BAT_ID = Column(String(8))
    AWAY_LINEUP4_FLD_CD = Column(Integer)
    AWAY_LINEUP5_BAT_ID = Column(String(8))
    AWAY_LINEUP5_FLD_CD = Column(Integer)
    AWAY_LINEUP6_BAT_ID = Column(String(8))
    AWAY_LINEUP6_FLD_CD = Column(Integer)
    AWAY_LINEUP7_BAT_ID = Column(String(8))
    AWAY_LINEUP7_FLD_CD = Column(Integer)
    AWAY_LINEUP8_BAT_ID = Column(String(8))
    AWAY_LINEUP8_FLD_CD = Column(Integer)
    AWAY_LINEUP9_BAT_ID = Column(String(8))
    AWAY_LINEUP9_FLD_CD = Column(Integer)
    HOME_LINEUP1_BAT_ID = Column(String(8))
    HOME_LINEUP1_FLD_CD = Column(Integer)
    HOME_LINEUP2_BAT_ID = Column(String(8))
    HOME_LINEUP2_FLD_CD = Column(Integer)
    HOME_LINEUP3_BAT_ID = Column(String(8))
    HOME_LINEUP3_FLD_CD = Column(Integer)
    HOME_LINEUP4_BAT_ID = Column(String(8))
    HOME_LINEUP4_FLD_CD = Column(Integer)
    HOME_LINEUP5_BAT_ID = Column(String(8))
    HOME_LINEUP5_FLD_CD = Column(Integer)
    HOME_LINEUP6_BAT_ID = Column(String(8))
    HOME_LINEUP6_FLD_CD = Column(Integer)
    HOME_LINEUP7_BAT_ID = Column(String(8))
    HOME_LINEUP7_FLD_CD = Column(Integer)
    HOME_LINEUP8_BAT_ID = Column(String(8))
    HOME_LINEUP8_FLD_CD = Column(Integer)
    HOME_LINEUP9_BAT_ID = Column(String(8))
    HOME_LINEUP9_FLD_CD = Column(Integer)
    AWAY_FINISH_PIT_ID = Column(String(8))
    HOME_FINISH_PIT_ID = Column(String(8))


class Parkcode(Base):
    __tablename__ = 'parkcodes'

    PARKID = Column(String(6), primary_key=True)
    NAME = Column(String(255))
    AKA = Column(String(255))
    CITY = Column(String(100))
    STATE = Column(String(3))
    START = Column(String(11))
    END = Column(String(11))
    LEAGUE = Column(String(3))
    NOTES = Column(String(255))


t_rosters = Table(
    'rosters', metadata,
    Column('YEAR', Integer),
    Column('PLAYER_ID', String(8)),
    Column('LAST_NAME_TX', String(25), index=True),
    Column('FIRST_NAME_TX', String(25), index=True),
    Column('BAT_HAND_CD', String(1)),
    Column('PIT_HAND_CD', String(1)),
    Column('TEAM_TX', String(3)),
    Column('POS_TX', String(5)),
    Index('index_full_name_tx_year', 'FIRST_NAME_TX', 'LAST_NAME_TX', 'YEAR'),
    Index('index_full_name_tx', 'FIRST_NAME_TX', 'LAST_NAME_TX')
)


t_teams = Table(
    'teams', metadata,
    Column('TEAM_ID', String(3)),
    Column('LG_ID', String(1)),
    Column('LOC_TEAM_TX', String(30)),
    Column('NAME_TEAM_TX', String(30))
)
