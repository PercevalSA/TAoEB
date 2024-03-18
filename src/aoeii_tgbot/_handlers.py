
from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def register_handlers(application: ApplicationBuilder):
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)