from env import EmailEnv

env = EmailEnv()

# START block
print("[START] task=email_triage", flush=True)

# Reset environment
obs = env.reset()

# Simple agent logic
text = obs["text"]

if "meeting" in text.lower():
    action = {"label": "important", "reply": "Sure, I will attend the meeting."}
elif "lottery" in text.lower():
    action = {"label": "spam", "reply": "This looks like spam."}
else:
    action = {"label": "normal", "reply": "Sounds good!"}

# Step
reward = env.step(action)

# STEP block
print(f"[STEP] reward={reward}", flush=True)

# END block
print(f"[END] score={reward}", flush=True)
