class OpenEnv:
    def __init__(self):
        self.state = {}

    def reset(self):
        self.state = {"step": 0}
        return self.state

    def step(self, action):
        self.state["step"] += 1
        reward = 1
        done = self.state["step"] >= 5
        return self.state, reward, done, {}