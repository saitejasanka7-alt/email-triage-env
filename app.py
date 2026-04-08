from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv

app = FastAPI()
env = EmailEnv()

class Action(BaseModel):
    label: str
    reply: str

@app.post("/reset")
@app.get("/reset")   # <-- ADD THIS LINE (IMPORTANT)
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
@app.get("/step")    # <-- ADD THIS LINE (IMPORTANT)
def step(action: Action = None):
    if action is None:
        return {"error": "No action provided"}
    
    reward = env.step(action.dict())
    return {"reward": reward}

@app.get("/")
def home():
    return {"message": "Email Triage AI Environment Running"}
