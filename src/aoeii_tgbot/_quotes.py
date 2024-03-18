from pathlib import Path
from random import choice

DEFAULT_QUOTE_FOLDER = Path('/workspaces/TAoEB/sounds')

def download_quotes():
    """Download AoE2 quotes from the internet."""
    pass

def get_random_quote(quote_folder: Path = DEFAULT_QUOTE_FOLDER) -> Path:
    """Return a random AoE2 quote audio file."""
    
    # get a random mp3 file in quote_folder
    quote_files = list(quote_folder.glob('*.wav'))
    return choice(quote_files)