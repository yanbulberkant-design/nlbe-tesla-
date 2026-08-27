import os
import requests

# Haal je Telegram Bot Token en Chat ID uit de instellingen (of vul ze hier direct in)
TOKEN = os.environ.get("TELEGRAM_TOKEN", "8967482066:AAH...") # Vervang eventueel met je echte token
CHAT_ID = "@NLBEFSD"

def send_telegram_message():
    message = "🚀 Tesla NL/BE FSD Bot is online en operationeel! Dit is een geautomatiseerde testmelding."
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Bericht succesvol verzonden naar Telegram!")
    else:
        print(f"Fout bij verzenden: {response.text}")

if __name__ == "__main__":
    send_telegram_message()
