from uuid import uuid4
import lorem
from schemas.game import GameLongDescription, GameShortDescription, Game


class GameController:

    @staticmethod
    async def get_game_by_name(name: str) -> GameLongDescription:
        title = name
        short_description = lorem.paragraph()
        long_description = lorem.text()
        game = Game(title=title, shortDescription=short_description,
                    longDescription=long_description)
        return GameLongDescription(uuid=uuid4().__str__(), long_description=game.longDescription)

    @ staticmethod
    async def get_games() -> list[GameShortDescription]:
        games = []
        games_short = []
        for i in range(0, 10):
            title = lorem.sentence().split(" ")[0]
            short_description = lorem.paragraph()
            long_description = lorem.text()
            games.append(Game(title=title, shortDescription=short_description,
                              longDescription=long_description))
        for i in range(0, 10):
            games_short.append(GameShortDescription(
                uuid=uuid4().__str__(), short_description=games[i].shortDescription))
        return games_short
