import random
from grader import grade_easy, grade_medium, grade_hard

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

        # randomly assign task
        self.task = random.choice(["easy", "medium", "hard"])

        return {
            "text": self.current["text"],
            "task": self.task
        }

    def step(self, action):
        expected = self.current

        if self.task == "easy":
            score = grade_easy(action, expected)
        elif self.task == "medium":
            score = grade_medium(action, expected)
        else:
            score = grade_hard(action, expected)

        # ensure score strictly between (0,1)
        if score <= 0:
            score = 0.1
        elif score >= 1:
            score = 0.9

        return score
