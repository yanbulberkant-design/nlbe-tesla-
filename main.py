from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TELEGRAM_TOKEN = "8967482066:AAGmGvB-Pb4BpIu9EhiVB8KAuSUuZnDJyGs"
CHANNEL_ID = "@NLBEFSD" 

bot = Bot(token=TELEGRAM_TOKEN)

def send_test_update():
    version = "2026.27.100.1"
    old_pct = 0.8
    new_pct = 1.2
    diff_pct = round(new_pct - old_pct, 2)
    
    message = (
        f"🚨 **Ongoing rollout for {version}**\n"
        f"Fleet: {old_pct}% ➔ {new_pct}% (+{diff_pct}%)\n"
        f"Pending: 0.5%\n"
        f"Installed: 0.7%\n"
        f"Model 3: 38%, Y: 37%, S: 17%, X: 8%"
    )
    
    keyboard = [
        [
            InlineKeyboardButton("TeslaFi", url="https://www.teslafi.com/firmware.php"),
            InlineKeyboardButton("NL-BE Inside", url="https://t.me/NLBEFSD")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
        print("✅ Gelukt! Het testbericht is verzonden naar @NLBEFSD!")
    except Exception as e:
        print(f"❌ Oeps, er ging iets mis: {e}")

if __name__ == "__main__":
    send_test_update()
