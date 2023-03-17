from fastapi import HTTPException
from fastapi import APIRouter
from schemas.game import GameShortDescription, GameLongDescription
from controllers.game import GameController


router = APIRouter()


@router.get("/games", response_model=list[GameShortDescription], tags=["games"])
async def get_games():
    games = await GameController.get_games()
    return games


@router.get("/games/{name}", response_model=GameLongDescription, tags=["games"])
async def get_game(name: str):
    game = await GameController.get_game_by_name(name=name)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game
