
import logging
from pathlib import Path
from telegram.ext import ApplicationBuilder
from os import environ

from ._bootstrap import install_sounds
from ._handlers import register_handlers

DEFAULT_TOKEN_FILE = Path('token.txt')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_token(token_file: Path) -> str:
    token = environ.get('TGB_TOKEN')
    if token is not None:
        return token

    logger.info("TGB_TOKEN not present in environment, using token from file.")
    if not token_file.exists():
        raise FileNotFoundError(f"Token file not found: {token_file}")

    return token_file.read_text().strip()

if __name__ == '__main__':
    install_sounds()
    application = ApplicationBuilder().token(get_token(DEFAULT_TOKEN_FILE)).build()
    register_handlers(application)
    application.run_polling()