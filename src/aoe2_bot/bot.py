import logging
from pathlib import Path
from telegram.ext import ApplicationBuilder
from os import environ

from ._bootstrap import bootstrap
from ._handlers import register_handlers


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def get_token() -> str:
    token = environ.get("TGB_TOKEN")
    if token is None:
        error = "TGB_TOKEN not present in environment. Please export it or set it in an env file"
        logger.error(error)
        raise EnvironmentError(error)
    return token


if __name__ == "__main__":
    bootstrap()
    application = ApplicationBuilder().token(get_token()).build()
    register_handlers(application)
    logger.info("Starting polling...")
    application.run_polling()
