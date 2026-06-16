import random
import requests
import urllib.parse


PROMPTS = [
    "Write a motivational fitness Telegram post with emojis (maximum 5 lines).",
    "Write an inspiring gym quote with emojis.",
    "Create a short bodybuilding motivation post.",
    "Write a fitness discipline message for beginners.",
    "Write a powerful health motivation post."
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

        return response.text.strip()

    except Exception as e:
        print(e)

        return (
            "💪 Stay consistent.\n"
            "🏋️ Train hard.\n"
            "🔥 Results come to those who never quit."
        )


def generate_image():
    prompt = random.choice([
        "muscular athlete lifting weights in gym",
        "fitness motivation poster",
        "bodybuilder training with cinematic lighting",
        "healthy lifestyle fitness art",
        "gym workout inspiration"
    ])

    return (
        "https://image.pollinations.ai/prompt/"
        + urllib.parse.quote(prompt)
    )