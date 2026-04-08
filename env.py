import random

class EmailEnv:
    def __init__(self):
        self.emails = [
            {
                "text": "Meeting at 5 PM, please attend",
                "label": "important",
                "reply": "Sure, I will attend the meeting."
            },
            {
                "text": "Congratulations! You won a lottery",
                "label": "spam",
                "reply": "This looks like spam."
            },
            {
                "text": "Lunch tomorrow?",
                "label": "normal",
                "reply": "Sounds good!"
            }
        ]

    def reset(self):
        self.current = random.choice(self.emails)
        return {"text": self.current["text"]}

    def step(self, action):
        reward = 0

        if action["label"] == self.current["label"]:
            reward += 0.5

        if action["reply"] == self.current["reply"]:
            reward += 0.5

        return reward
