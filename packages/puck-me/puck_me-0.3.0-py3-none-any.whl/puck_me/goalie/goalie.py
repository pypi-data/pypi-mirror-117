from puck_me.player.player import Player
from bs4.element import ResultSet
from puck_me.goalie.goalie_game import GoalieGame
import pandas as pd
from enum import Enum
from puck_me.lib.split_types import SplitType
from puck_me.lib.utils import convert_stat_to_type


class SplitCol(Enum):
    VALUE = "Value"
    GAMES_PLAYED = "GP"
    WINS = "W"
    LOSSES = "L"
    TIE_LOSSES = "T/O"
    GOALS_AGAINST = "GA"
    SHOTS_FACED = "SA"
    SAVES = "SV"
    SAVE_PERCENT = "SV%"
    GOALS_AGAINST_AVG = "GAA"
    SHUTOUTS = "SO"
    PENALTY_MINS = "PIM"
    TIME_ON_ICE = "TOI"
    GOALS_AGAINST_EV = "EV GA"
    GOALS_AGAINST_PP = "PP GA"
    GOALS_AGAINST_SH = "SH GA"


class GoalieSplit:
    def __init__(self, split_table_series: pd.Series) -> None:
        self.value = convert_stat_to_type(split_table_series[SplitCol.VALUE.value], str)
        self.games_played = convert_stat_to_type(
            split_table_series[SplitCol.GAMES_PLAYED.value], int
        )
        self.wins = convert_stat_to_type(split_table_series[SplitCol.WINS.value], int)
        self.losses = convert_stat_to_type(
            split_table_series[SplitCol.LOSSES.value], int
        )
        self.tie_losses = convert_stat_to_type(
            split_table_series[SplitCol.TIE_LOSSES.value], int
        )
        self.goals_against = convert_stat_to_type(
            split_table_series[SplitCol.GOALS_AGAINST.value], int
        )
        self.shots_faced = convert_stat_to_type(
            split_table_series[SplitCol.SHOTS_FACED.value], int
        )
        self.saves = convert_stat_to_type(split_table_series[SplitCol.SAVES.value], int)
        self.save_percent = convert_stat_to_type(
            split_table_series[SplitCol.SAVE_PERCENT.value], float
        )
        self.goals_against_avg = convert_stat_to_type(
            split_table_series[SplitCol.GOALS_AGAINST_AVG.value], float
        )
        self.shutouts = convert_stat_to_type(
            split_table_series[SplitCol.SHUTOUTS.value], int
        )
        self.penalty_mins = convert_stat_to_type(
            split_table_series[SplitCol.PENALTY_MINS.value], int
        )
        self.time_on_ice = convert_stat_to_type(
            split_table_series[SplitCol.TIME_ON_ICE.value], str
        )
        self.goals_against_ev = convert_stat_to_type(
            split_table_series[SplitCol.GOALS_AGAINST_EV.value], int
        )
        self.goals_against_pp = convert_stat_to_type(
            split_table_series[SplitCol.GOALS_AGAINST_PP.value], int
        )
        self.goals_against_sh = convert_stat_to_type(
            split_table_series[SplitCol.GOALS_AGAINST_SH.value], int
        )


class Goalie(Player):

    ##########################
    # Public Functions
    ##########################

    def gamelog(self, year: str = None) -> list[GoalieGame]:
        if not year:
            year = self._year
        if not self._gamelog_regular_season and not self._gamelog_playoffs:
            self.__populate_gamelogs(year)
        return self._gamelog_regular_season + self._gamelog_playoffs

    def gamelog_playoffs(self, year: str = None) -> list[GoalieGame]:
        if not year:
            year = self._year
        if not self._gamelog_regular_season and not self._gamelog_playoffs:
            self.__populate_gamelogs(year)
        return self._gamelog_playoffs

    def gamelog_regular_season(self, year: str = None) -> list[GoalieGame]:
        if not year:
            year = self._year
        if not self._gamelog_regular_season and not self._gamelog_playoffs:
            self.__populate_gamelogs(year)
        return self._gamelog_regular_season

    def games_played(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.games_played

    def wins(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.wins

    def losses(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.losses

    def tie_losses(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.tie_losses

    def goals_against(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.goals_against

    def shots_faced(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.shots_faced

    def saves(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.saves

    def save_percent(self, year: str = None) -> float:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.save_percent

    def goals_against_avg(self, year: str = None) -> float:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.goals_against_avg

    def shutouts(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.shutouts

    def penalty_mins(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.penalty_mins

    def time_on_ice(self, year: str = None) -> str:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.time_on_ice

    def goals_against_ev(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.goals_against_ev

    def goals_against_pp(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.goals_against_pp

    def goals_against_sh(self, year: str = None) -> int:
        if not self._season_split or year != self._year:
            self._season_split = self.splits(SplitType.SEASON, year)[0]
        return self._season_split.goals_against_sh

    def splits(self, split_type: SplitType, year: str = None) -> list[GoalieSplit]:
        split_df = self._split_df_lookup(year, split_type)
        return self.__split_df_to_rows(split_df)

    ##########################
    # Gamelog Section
    ##########################

    def __populate_gamelogs(self, year: str) -> None:
        if not self._gamelog_playoffs or not self._gamelog_regular_season:
            soup = self._request_player_gamelog_page(year)
            reg_season_rows = self._regular_season_games(soup)
            playoff_rows = self._playoff_games(soup)
            self._gamelog_regular_season = self.__get_games_by_table_rows(
                reg_season_rows, is_playoff=False
            )
            self._gamelog_playoffs = self.__get_games_by_table_rows(
                playoff_rows, is_playoff=True
            )

    def __get_games_by_table_rows(
        self, rows: ResultSet, is_playoff: bool
    ) -> list[GoalieGame]:
        games = []
        for row_html in rows:
            game = GoalieGame(row_html, is_playoff)
            games += [game]
        return games

    ##########################
    # Splits Section
    ##########################

    def __split_df_to_rows(self, split_df: pd.DataFrame) -> list[GoalieSplit]:
        rows = []
        for index, series in split_df.iterrows():
            rows += [GoalieSplit(series)]
        return rows
