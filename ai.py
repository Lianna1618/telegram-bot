import random
import requests
import urllib.parse

PROMPTS = [
    "Write a short inspiring Telegram post about the beauty of nature with emojis (maximum 5 lines).",
    "Write a motivational post encouraging people to spend more time outdoors.",
    "Create a healthy lifestyle tip focused on eating natural and nutritious foods.",
    "Write an inspiring message about fresh fruits and vegetables for a Telegram channel.",
    "Generate a positive post about enjoying peaceful landscapes and fresh air.",
    "Write a short post about the benefits of drinking enough water and eating healthy.",
    "Create a motivational message about living in harmony with nature.",
    "Write a calming post about forests, mountains, and finding inner peace.",
    "Generate an educational post about one healthy superfood and its benefits.",
    "Write a positive message encouraging healthy eating habits every day.",
    "Create a short wellness post about balancing nutrition, movement, and rest.",
    "Write a relaxing morning inspiration inspired by sunrise in nature.",
    "Generate a post about seasonal fruits and why they are good for your health.",
    "Write an uplifting message about choosing healthy food over processed food.",
    "Create a Telegram post celebrating beautiful natural landscapes around the world."
]

IMAGE_PROMPTS = [
    "majestic mountain landscape at sunrise, ultra realistic, vibrant colors",
    "peaceful forest with sun rays shining through tall trees, cinematic photography",
    "crystal clear lake surrounded by mountains, breathtaking nature",
    "healthy breakfast with fresh fruits, oatmeal, berries and orange juice, professional food photography",
    "colorful assortment of fresh vegetables on a wooden table, natural lighting",
    "organic salad with avocado, tomatoes, cucumbers and herbs, gourmet presentation",
    "basket full of seasonal fruits in a blooming garden",
    "tropical beach with turquoise water, palm trees and white sand",
    "waterfall deep inside a lush green forest, magical atmosphere",
    "golden wheat field under a dramatic sunset sky",
    "lavender fields during golden hour, stunning landscape photography",
    "fresh smoothie bowl with berries, kiwi, banana and granola, healthy food photography",
    "organic farmers market with colorful fruits and vegetables",
    "beautiful autumn forest with vibrant orange and red leaves",
    "wildflower meadow beneath snow-capped mountains, ultra detailed"
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