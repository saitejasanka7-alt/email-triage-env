from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv

app = FastAPI()
env = EmailEnv()

class Action(BaseModel):
    label: str
    reply: str

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs
    }

@app.post("/step")
def step(action: Action):
    reward = env.step(action.dict())
    return {
        "reward": reward
    }

@app.get("/")
def home():
    return {"status": "running"}

# IMPORTANT: entrypoint function
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
