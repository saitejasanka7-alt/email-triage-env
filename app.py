from fastapi import FastAPI

app = FastAPI()

# GLOBAL STATE
state = {}

@app.get("/")
def home():
    return {"status": "running"}

# REQUIRED: RESET API
@app.post("/reset")
def reset():
    global state
    state = {"email": "Sample email text"}
    return state

# REQUIRED: STEP API
@app.post("/step")
def step(action: dict):
    # simple dummy response
    return {
        "observation": state,
        "reward": 0.5,
        "done": False,
        "info": {}
    }

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
