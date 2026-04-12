def step(self, action):
    reward = 0.1  # base reward (avoid 0)

    if action["label"] == self.current["label"]:
        reward += 0.4

    if action["reply"] == self.current["reply"]:
        reward += 0.4

    return reward
