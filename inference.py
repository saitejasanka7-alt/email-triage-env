from env import EmailEnv

env = EmailEnv()

try:
    print("[START] task=email_triage", flush=True)

    obs = env.reset()
    text = obs["text"]

    # simple rule-based logic (NO API)
    if "meeting" in text.lower():
        action = {"label": "important", "reply": "Sure, I will attend the meeting."}
    elif "lottery" in text.lower():
        action = {"label": "spam", "reply": "This looks like spam."}
    else:
        action = {"label": "normal", "reply": "Sounds good!"}

    reward = env.step(action)

    print(f"[STEP] reward={reward}", flush=True)
    print(f"[END] score={reward}", flush=True)

except Exception as e:
    print("[ERROR]", str(e), flush=True)

