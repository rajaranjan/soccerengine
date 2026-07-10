from pydantic import BaseModel
from typing import Optional


class Player(BaseModel):
    
    player_id: int
    name: str
    goals: int
    passes: int
    assists: int
    shots: int
    position: str
    age: int
    leagues: list[str]
    matches_own: int
