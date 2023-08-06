from puck_me.goalies import Goalies
from puck_me.goalie.goalie import Goalie
from puck_me.skaters import Skaters
from puck_me.skater.skater import Skater


class Players:
    @staticmethod
    def all_goalies(year: str = None) -> list[Goalie]:
        return Goalies.all_goalies(year)

    @staticmethod
    def all_skaters(year: str = None) -> list[Skater]:
        return Skaters.all_skaters(year)
