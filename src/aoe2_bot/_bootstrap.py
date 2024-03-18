from pathlib import Path
from zipfile import ZipFile
import requests
import logging

logger = logging.getLogger(__name__)

media_base_url = (
    "https://media.githubusercontent.com/media/PercevalSA/TAoEB/main/assets/sounds/"
)
# named are generic sounds, unnamed are all civilization sounds
media_archives = ["named.zip"] # "unnamed.zip" is too big for now


def unzip(zip_file: Path, dest_folder: Path, *, remove_zip: bool = False) -> None:
    logger.info(f"Unzipping {zip_file} to {dest_folder}")
    with ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(dest_folder)
    if remove_zip:
        logger.info(f"Removing {zip_file}")
        zip_file.unlink()


def download_zip(url: str, dest_folder: Path) -> Path:
    logger.info(f"Downloading {url} to {dest_folder}")
    local_filename = dest_folder / url.split("/")[-1]
    # NOTE the stream=True parameter below to avoid storing the entire file into memory at once
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    
    logger.info(f"Download {local_filename.name} complete")
    return local_filename


def create_sounds_folder() -> Path:
    logger.info("Creating sounds folder if missing")
    sounds_folder = Path(__file__).parent / "sounds"
    sounds_folder.mkdir(exist_ok=True)
    return sounds_folder

def finish_bootstrap(sounds_folder: Path) -> None:
    (sounds_folder / "installation_complete").touch()
    logger.info("Audio files bootstrap complete")

def check_bootstrap(sounds_folder: Path) -> bool:
    return (sounds_folder / "installation_complete").exists()


def install_sounds(sounds_folder: Path) -> None:
    logger.info("Installing audio files...")
    for archive in media_archives:
        sounds_url = media_base_url + archive
        zip_file = download_zip(sounds_url, sounds_folder)
        unzip(zip_file , sounds_folder, remove_zip=True)


def bootstrap() -> None:
    sounds_folder = create_sounds_folder()
    if check_bootstrap(sounds_folder):
        logger.info("Audio files already installed")
        return
    install_sounds(sounds_folder)
    finish_bootstrap(sounds_folder)