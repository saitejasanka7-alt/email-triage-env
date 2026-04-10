class EmailEnv:
    def __init__(self):
        self.tasks = ["easy_task", "medium_task", "hard_task"]

    def reset(self):
        return {"text": "Sample email"}

    def step(self, action):
        return 0.5
