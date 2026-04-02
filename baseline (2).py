from env import EmailEnv

env = EmailEnv()
email = env.reset()

print("Email:", email["text"])

# simple AI
if "meeting" in email["text"].lower():
    action = {"label": "important", "reply": "Sure, I will attend the meeting."}
elif "lottery" in email["text"].lower():
    action = {"label": "spam", "reply": "This looks like spam."}
else:
    action = {"label": "normal", "reply": "Sounds good!"}

print("AI Action:", action)

reward = env.step(action)

print("Reward:", reward)
