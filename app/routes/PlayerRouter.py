from fastapi import APIRouter, HTTPException
from app.models import Player
from app.services import list_players, get_player, create_player

PlayerRouter = APIRouter()


@PlayerRouter.get("/")
def read_players(position: str | None = None):
    return list_players(position)

@PlayerRouter.get("/{player_id}")
def read_player(player_id: int):
    player = get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@PlayerRouter.post("/")
def add_player(player: Player):
    # This is a simplified example; in a real application, you would need to associate the player with a team
    return player