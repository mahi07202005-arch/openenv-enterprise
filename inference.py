from fastapi import FastAPI
from pydantic import BaseModel
from env.core_env import OpenEnv
from env.models import simple_model

app = FastAPI()

env = OpenEnv()

class StepRequest(BaseModel):
    action: str = ""

# ✅ IMPORTANT: Explicit POST handler
@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "state": state
    }

# ✅ IMPORTANT: Correct request format
@app.post("/step")
def step(req: StepRequest):
    action = req.action if req.action else "Say Hello"

    output = simple_model(action)
    state, reward, done, _ = env.step(output)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "output": output
    }

# ✅ THIS FIXES METHOD ISSUE
@app.get("/")
def root():
    return {"message": "OpenEnv API running"}