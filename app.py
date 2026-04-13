from fastapi import FastAPI

app = FastAPI()

state = {}

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    global state
    state = {"email": "Sample email"}
    return state

@app.post("/step")
def step(action: dict):
    return {
        "observation": state,
        "reward": 0.5,
        "done": False,
        "info": {}
    }

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

# 🚨 THIS LINE IS THE FIX
if __name__ == "__main__":
    main()
