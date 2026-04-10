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
        score = 0.0

        if action["label"] == self.current["label"]:
            score += 0.5

        if action["reply"] == self.current["reply"]:
            score += 0.4

        # ensure score strictly between (0,1)
        if score == 0:
            score = 0.1
        elif score >= 0.9:
            score = 0.9

        return score
