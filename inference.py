from fastapi import FastAPI
from pydantic import BaseModel
from env.core_env import OpenEnv
from env.models import simple_model

app = FastAPI()

env = OpenEnv()

class ActionRequest(BaseModel):
    action: str = ""

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(req: ActionRequest):
    action = req.action if req.action else "Say Hello"
    
    model_output = simple_model(action)
    state, reward, done, _ = env.step(model_output)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "output": model_output
    }