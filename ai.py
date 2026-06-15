import requests
import urllib.parse
import random

# 🧠 TEXT AI (FREE — no API, no Ollama)
def generate_text():
    prompts = [
        "Write a short viral Telegram post about fitness motivation 💪🔥 max 5 lines",
        "Give a powerful gym motivation message with emojis 💥💪",
        "Write a health and discipline quote for gym lovers 🏋️‍♂️",
        "Create a motivational fitness post for beginners 🏃‍♂️🔥",
        "Write a short bodybuilding motivation message with energy 💪⚡"
    ]

    prompt = random.choice(prompts)

    try:
        r = requests.post(
            "https://text.pollinations.ai/",
            json={"prompt": prompt},
            timeout=30
        )

        if r.status_code == 200:
            return r.text

    except Exception as e:
        print("AI error:", e)

    # fallback (always works)
    return "💪 No excuses. Train hard. Stay consistent. Build your dream body!"


# 🖼 IMAGE AI (FREE Pollinations)
def generate_image(prompt):
    safe_prompt = urllib.parse.quote(prompt)

    return f"https://image.pollinations.ai/prompt/{safe_prompt}"