import random
import requests
import urllib.parse

PROMPTS = [
    "Write a motivational fitness Telegram post with emojis (maximum 5 lines).",
    "Write an inspiring gym quote with emojis.",
    "Create a short bodybuilding motivation post.",
    "Write a fitness discipline message for beginners.",
    "Write a powerful health motivation post.",
    "Write a motivational post about consistency and discipline in fitness.",
    "Create an energetic fitness motivation message for the morning.",
]

IMAGE_PROMPTS = [
    "muscular athlete lifting weights in modern gym, cinematic lighting, epic atmosphere",
    "determined fitness model training hard, sweat and motivation, dramatic lighting",
    "bodybuilder posing with intense expression, gym background, high detail",
    "powerful fitness transformation motivation poster style",
    "athletic person running at sunrise, motivational fitness vibe",
    "strong woman doing pull-ups, empowering fitness aesthetic",
    "muscular man deadlifting heavy weights, intense gym atmosphere",
]

def generate_text():
    prompt = random.choice(PROMPTS)
    try:
        response = requests.post(
            "https://text.pollinations.ai/",
            json={"prompt": prompt},
            timeout=30
        )
        response.raise_for_status()
        text = response.text.strip()
        # Ensure it doesn't exceed Telegram caption limit (~1024 chars)
        if len(text) > 900:
            text = text[:897] + "..."
        return text
    except Exception as e:
        print("AI text error:", e)
        return (
            "💪 **Stay consistent.**\n"
            "🏋️ **Train hard.**\n"
            "🔥 **Results come to those who never quit.**\n\n"
            "#FitnessMotivation"
        )


def generate_image_url():
    prompt = random.choice(IMAGE_PROMPTS)
    # Add some randomization to avoid repetitive images
    seed = random.randint(1, 999999)
    return (
        f"https://image.pollinations.ai/prompt/"
        f"{urllib.parse.quote(prompt)}"
        f"?seed={seed}&width=1080&height=1080&nologo=true"
    )