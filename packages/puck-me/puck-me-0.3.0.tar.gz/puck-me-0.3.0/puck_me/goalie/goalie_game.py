from bs4.element import Tag
from puck_me.lib import utils
from puck_me.game.game import Game


class GoalieGame(Game):
    def __init__(self, row_html: Tag, is_playoff: bool) -> None:
        super().__init__(row_html, is_playoff)
        self.__populate_goalie_stats(row_html)

    def __str__(self) -> str:
        pub_dict = dict()
        for (key, value) in self.__dict__.items():
            if not key.startswith("_GoalieGame"):
                pub_dict[key] = value
        return str(pub_dict)

    def __populate_goalie_stats(self, row_html: Tag):
        self.decision = utils.parse_data_stat(row_html, "decision", str)
        self.goals_against = utils.parse_data_stat(row_html, "goals_against", int)
        self.shots_against = utils.parse_data_stat(row_html, "shots_against", int)
        self.saves = utils.parse_data_stat(row_html, "saves", int)
        self.save_pct = utils.parse_data_stat(row_html, "save_pct", float)
        self.shutouts = utils.parse_data_stat(row_html, "shutouts", int)
