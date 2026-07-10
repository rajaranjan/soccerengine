from app.models import Player
from app.utils.players_data import PLAYERS


_PLAYERS: list[Player] = PLAYERS

def ranking_players() -> list[Player]:
    return sorted(_PLAYERS, key=lambda player: player.rating, reverse=True)

def list_players() -> list[Player]:
    return _PLAYERS

def get_player(player_id: int) -> Player | None:
    return next((player for player in _PLAYERS if player.player_id == player_id), None)

def create_player(player: Player) -> Player:
    _PLAYERS.append(player)
    return player