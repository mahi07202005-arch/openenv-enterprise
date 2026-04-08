from fastapi import FastAPI
from pydantic import BaseModel
from env.core_env import OpenEnv
from env.models import simple_model

app = FastAPI()

env = OpenEnv()

class StepRequest(BaseModel):
    action: str = ""

@app.get("/")
def root():
    return {"status": "running"}

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
        "reward": float(reward),
        "done": bool(done),
        "info": {"output": output}
    }if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)