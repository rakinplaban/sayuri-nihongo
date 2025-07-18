import random
import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# 🔗 Your Discord webhook URL here
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Word list (kanji, kana, romaji, meaning)
words = [
    ("勉強", "べんきょう", "benkyou", "study"),
    ("頑張って", "がんばって", "ganbatte", "do your best!"),
    ("時間", "じかん", "jikan", "time"),
    ("日本語", "にほんご", "nihongo", "Japanese (language)"),
    ("今日", "きょう", "kyou", "today"),
    ("覚える", "おぼえる", "oboeru", "to memorize"),
]

messages = [
    "Sayuri says: “Even 5 minutes of 勉強 is 勝利 (victory)!”",
    "Sayuri believes in you! 今日もがんばって！💪",
    "Don't worry if it's slow — step by step is the Sayuri way 🌸",
    "Language is love. Treat it like art, not a chore!",
]

# Seed for consistency
random.seed(datetime.date.today().toordinal())
kanji, kana, romaji, meaning = random.choice(words)
message = random.choice(messages)

# Compose message
content = (
    f"📖 **Today's Word:** {kanji} ({kana} / {romaji})\n"
    f"💬 **Meaning:** {meaning}\n\n"
    f"🌸 {message}"
)

# Send to Discord
payload = {
    "username": "Sayuri Hayasaka",
    "content": content
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print("✅ Sayuri sent the message successfully!")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
