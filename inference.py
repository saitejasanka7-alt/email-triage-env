from env import EmailEnv
import os
from openai import OpenAI

# ✅ Use validator proxy (MANDATORY)
client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=os.environ["API_BASE_URL"],
)

def call_llm(text):
    res = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Classify the email into spam, important, or normal and give a short reply in JSON format: {label, reply}"
            },
            {"role": "user", "content": text},
        ],
        temperature=0,
    )
    return res.choices[0].message.content


env = EmailEnv()

print("[START] task=email_triage", flush=True)

obs = env.reset()
text = obs["text"]

# ✅ CALL LLM (THIS FIXES YOUR ERROR)
response = call_llm(text)

# simple parsing (safe fallback)
import json
try:
    parsed = json.loads(response)
    action = {
        "label": parsed.get("label", "normal"),
        "reply": parsed.get("reply", "OK"),
    }
except:
    action = {"label": "normal", "reply": "OK"}

reward = env.step(action)

print(f"[STEP] reward={reward}", flush=True)
print(f"[END] score={reward}", flush=True)


