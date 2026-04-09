from env import EmailEnv

env = EmailEnv()
obs = env.reset()

# simple rule-based agent
def agent(obs):
    text = obs["email_text"].lower()

    if "meeting" in text:
        return {
            "label": "important",
            "reply": "Sure, I will attend the meeting."
        }
    elif "lottery" in text:
        return {
            "label": "spam",
            "reply": "This looks like spam."
        }
    else:
        return {
            "label": "normal",
            "reply": "Sounds good!"
        }

action = agent(obs)
next_obs, reward, done, _ = env.step(action)

print("Observation:", obs)
print("Action:", action)
print("Reward:", reward)
