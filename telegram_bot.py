from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Функция старта игры
async def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton("Начать игру", web_app={'url': 'https://silence-creator.github.io/hoi4combat/'})
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Добро пожаловать в Hamster Kombat! Нажмите кнопку ниже, чтобы начать игру.",
        reply_markup=reply_markup
    )

# Основная функция для запуска бота
def main():
    token = "7775350076:AAFupdYtqks3gJ_rPiPOfXTklxARzAlyg9Y"  # Замените на ваш токен
    app = ApplicationBuilder().token(token).build()

    # Добавление обработчика команд
    app.add_handler(CommandHandler("start", start))

    # Запуск бота (polling)
    app.run_polling()

if __name__ == '__main__':
    main()