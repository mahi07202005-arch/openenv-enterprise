from fastapi import FastAPI
from pydantic import BaseModel
from env.core_env import OpenEnv
from env.models import simple_model

app = FastAPI()

env = OpenEnv()

class StepRequest(BaseModel):
    action: str = ""

@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "observation": state
    }

@app.post("/step")
def step(req: StepRequest):
    action = req.action if req.action else "Say Hello"

    output = simple_model(action)
    state, reward, done, _ = env.step(output)

    return {
        "observation": state,
        "reward": reward,
        "done": done,
        "info": {"output": output}
    }

@app.get("/")
def root():
    return {"message": "OpenEnv API running"}