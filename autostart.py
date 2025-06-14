import requests
import time

TELEGRAM_TOKEN = "7971605755:AAHAh9QO9BVS9dLAWYB4ZZ1XxCGZ-15Ut2M"
CHAT_ID = "-1002712669499"

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.get(url, params=payload)
    except Exception as e:
        print(f"Telegram error: {e}")

send_message("✅ Mining started in Codespace using XMRig!")

while True:
    send_message("⛏️ Miner still running — Worker: codespace")
    time.sleep(3600)