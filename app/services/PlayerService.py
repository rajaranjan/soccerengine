from app.models import Player
from app.utils.players_data import PLAYERS


def calculate_score(player: dict) -> int:
    # forward player ranking based on weighted factors
    wf_goals = 0.35
    wf_assists = 0.25
    wf_passes = 0.15
    wf_shots = 0.25

    # Midfielder player ranking based on weighted factors
    wm_goals = 0.25
    wm_assists = 0.35
    wm_passes = 0.25
    wm_shots = 0.15

    # Defender player ranking based on weighted factors
    wd_goals = 0.15
    wd_assists = 0.25
    wd_passes = 0.35
    wd_shots = 0.25

    # goalkeeper player ranking based on weighted factors
    wg_saves = 0.25
    wg_clean_sheets = 0.55
    wg_passes = 0.15

    if player["position"] == "Forward":
        score = wf_goals * player["goals"] + wf_assists * player["assists"] + wf_passes * player["assists"] + wf_shots * player["shots"]
        return score

    elif player["position"] == "Midfielder":
        score = wm_goals * player["goals"] + wm_assists * player["assists"] + wm_passes * player["assists"] + wm_shots * player["shots"]
        return score

    elif player["position"] == "Defender":
        score = wd_goals * player["goals"] + wd_assists * player["assists"] + wd_passes * player["assists"] + wd_shots * player["shots"]
        return score
            
    elif player["position"] == "Goalkeeper":
        score = wg_saves * player["saves"] + wg_clean_sheets * player["clean_sheets"] + wg_passes * player["assists"]
        return score

def list_players(position: str | None = None) -> list[Player]:
    
    players = []

    for player in PLAYERS:
        player["score"] = calculate_score(player)
        players.append(player)

    if position == "all":
        players = players
    elif position == "Forward":
        players = [player for player in players if player["position"] == "Forward"]
    elif position == "Midfielder":
        players = [player for player in players if player["position"] == "Midfielder"]
    elif position == "Defender":
        players = [player for player in players if player["position"] == "Defender"]
    elif position == "Goalkeeper":
        players = [player for player in players if player["position"] == "Goalkeeper"]

    players = sorted(players, key=lambda x: x["score"], reverse=True)
    return players

def get_player(player_id: int) -> Player | None:
    return next((player for player in _PLAYERS if player.player_id == player_id), None)

def create_player(player: Player) -> Player:
    _PLAYERS.append(player)
    return player