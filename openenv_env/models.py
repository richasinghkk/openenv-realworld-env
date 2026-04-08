from pydantic import BaseModel

# Observation returned by environment
class Observation(BaseModel):
    task_id: int
    input_data: str


# Action given by agent
class Action(BaseModel):
    response: str


# Reward returned
class Reward(BaseModel):
    score: float
    feedback: str