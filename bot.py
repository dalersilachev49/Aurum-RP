from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ТВОЙ_ТОКЕН"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Здравствуйте!\n\n"
        "📝 Пожалуйста, подробно опишите свою проблему.\n"
        "📸 Обязательно прикрепите доказательства (скриншоты, фото или видео).\n"
        "⏳ Администраторы рассмотрят ваше обращение.\n"
        "✅ Ответ поступит в течение одного часа.\n\n"
        "🙏 Спасибо за обращение!"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
