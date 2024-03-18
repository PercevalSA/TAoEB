
from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
from ._quotes import get_random_quote

aoe2_logo = "/workspaces/TAoEB/images/Age_of_Empires_2_Logo.png"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="À la bataille! Use /aoe to get a quote from Age of Empires II.")


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote_file = get_random_quote()
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=quote_file, title=quote_file.stem, thumbnail=aoe2_logo, disable_notification=True)

def register_handlers(application: ApplicationBuilder):
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('aoe', quote))