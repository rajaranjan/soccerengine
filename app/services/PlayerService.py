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
        return round(score, 2)

    elif player["position"] == "Midfielder":
        score = wm_goals * player["goals"] + wm_assists * player["assists"] + wm_passes * player["assists"] + wm_shots * player["shots"]
        return round(score, 2)

    elif player["position"] == "Defender":
        score = wd_goals * player["goals"] + wd_assists * player["assists"] + wd_passes * player["assists"] + wd_shots * player["shots"]
        return round(score, 2)
            
    elif player["position"] == "Goalkeeper":
        score = wg_saves * player["saves"] + wg_clean_sheets * player["clean_sheets"] + wg_passes * player["assists"]
        return round(score, 2)

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

    players = sorted(players, key=lambda player: player["score"], reverse=True)
    return players

def get_player(player_id: int) -> Player | None:
    player = next((player for player in PLAYERS if player["id"] == player_id), None)
    goalsData = []
    passesData = []
    assistData = []
    shotsData = []
    matchesData = []
    savesData = []
    cleansheetData = []

    if player["position"] == "Goalkeeper":
        GPLAYER = [p for p in PLAYERS if p.get("position") == "Goalkeeper"]
        
        for gPlayer in GPLAYER:
            savesobject = {
                "name": gPlayer["name"],
                "saves": gPlayer["saves"]
            }
            savesData.append(savesobject)

            cleansheetobject = {
                "name": gPlayer["name"],
                "clean_sheets": gPlayer["clean_sheets"]
            }
            cleansheetData.append(cleansheetobject)
            
            matchesobject = {
                "name": gPlayer["name"],
                "matches_own": gPlayer["matches_own"]
            }
            matchesData.append(matchesobject)

        player["savesData"] = savesData
        player["cleansheetData"] = cleansheetData
        player["matchesData"] = matchesData
    else:
        OPLAYER = [p for p in PLAYERS if p.get("position") == player["position"]]

        # print("OP", OPLAYER)
        for oPlayer in OPLAYER:
            # print("oo", oPlayer)
            goalsobject = {
                "name": oPlayer["name"],
                "goals": oPlayer["goals"]
            }
            goalsData.append(goalsobject)

            passesobject = {
                "name": oPlayer["name"],
                "passes": oPlayer["passes"]
            }
            passesData.append(passesobject)

            assistobject = {
                "name": oPlayer["name"],
                "assists": oPlayer["assists"]
            }
            assistData.append(assistobject)

            shotsobject = {
                "name": oPlayer["name"],
                "shots": oPlayer["shots"]
            }
            shotsData.append(shotsobject)

            matchesobject = {
                "name": oPlayer["name"],
                "matches_own": oPlayer["matches_own"]
            }
            matchesData.append(matchesobject)

        player["goalsData"] = goalsData
        player["passesData"] = passesData
        player["assistsData"] = assistData
        player["shotsData"] = shotsData
        player["matchesData"] = matchesData

    return player
