from pydantic import BaseModel
from typing import Optional


class Player(BaseModel):

    player_id: int
    name: str
    position: str
    age: int
    leagues: list[str]
    matches_own: int
    passes: int
    # Outfield player stats
    goals: int = 0
    assists: int = 0
    shots: int = 0
    # Goalkeeper stats
    saves: int = 0
    clean_sheets: int = 0
