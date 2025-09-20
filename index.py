from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "#news\n"
        "#ton\n"
        "#btc\n"
        "#educational\n\n"
        "✅ GENUINE SERVICE AVAILABLE ✅\n"
        "🔥 ONLY PAID SERVICE 🔥\n\n"
        "Servce xys available...\n\n"
        "💌 https://t.me/+g56yxbnFDbZiMTg1\n"
        "💌 https://t.me/+g56yxbnFDbZiMTg1\n"
        "💌 https://t.me/+g56yxbnFDbZiMTg1\n"
        "💌 https://t.me/+g56yxbnFDbZiMTg1\n"
        "💌 https://t.me/+g56yxbnFDbZiMTg1\n\n"
       
    )

    await update.message.reply_text(text, disable_web_page_preview=True)

# Main
if __name__ == "__main__":
    TOKEN = "8341942406:AAHfBTptoKOCZ-0_Tho_I3fSNQtT1z2OQoc"  # apna token dalna

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()
