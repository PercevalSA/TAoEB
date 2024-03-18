from telegram import Update
from telegram.constants import MessageEntityType
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
import logging
from pathlib import Path
from random import choice


logger = logging.getLogger(__name__)

assets_folder = Path(__file__).parent / "assets"
aoe2_logo = assets_folder / "images/Age_of_Empires_2_Logo.png"
sounds_folder = assets_folder / "sounds"


def get_random_sound() -> Path:
    """Return a random AoE2 quote audio file."""
    quote_files = list(sounds_folder.glob("*.wav"))
    return choice(quote_files)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="À la bataille! Use /aoe to get a quote from Age of Empires II.",
    )


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote_file = get_random_sound()
    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=quote_file,
        title=quote_file.stem,
        thumbnail=aoe2_logo,
        disable_notification=True,
    )


async def taunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Taunt command entities: {update.message.entities}")
    if update.message.entities[0].type != MessageEntityType.BOT_COMMAND:
        logger.warning("Not a bot command")
        return

    try:
        taunt_num = int(update.message.text.strip("/"))
    except ValueError as e:
        logger.error(f"Taunt command is not a number: {e}")

    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=assets_folder / "sounds/{taunt_num}.wav",
        title=f"Taunt {taunt_num}",
        thumbnail=aoe2_logo,
        disable_notification=True,
    )


def register_taunt_handlers(application: ApplicationBuilder):
    taunt_number: int = 100
    for i in range(1, taunt_number):
        application.add_handler(CommandHandler(f"{i}", taunt))


def register_handlers(application: ApplicationBuilder):
    logger.info("Registering handlers")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("aoe", quote))

    register_taunt_handlers(application)
