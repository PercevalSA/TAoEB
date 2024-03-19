import logging
from pathlib import Path
from zipfile import ZipFile

import requests

logger = logging.getLogger(__name__)

media_base_url = (
    "https://media.githubusercontent.com/media/PercevalSA/TAoEB/main/assets/"
)
# named are generic sounds, unnamed are all civilization sounds
media_archives = ["named.zip"]  # "unnamed.zip" is too big for now


def unzip(zip_file: Path, dest_folder: Path, *, remove_zip: bool = False) -> None:
    logger.info(f"Unzipping {zip_file} to {dest_folder}")
    with ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(dest_folder)
    if remove_zip:
        logger.info(f"Removing {zip_file}")
        zip_file.unlink()


def download_bin(url: str, dest_folder: Path) -> Path:
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


def create_media_folder() -> Path:
    logger.info("Creating sounds folder if missing")
    media_folder = Path(__file__).parent / "media"
    media_folder.mkdir(exist_ok=True)
    return media_folder


def finish_bootstrap(media_folder: Path) -> None:
    (media_folder / "installation_complete").touch()
    logger.info("Media files bootstrap complete")


def check_bootstrap(media_folder: Path) -> bool:
    return (media_folder / "installation_complete").exists()


def install_sounds(media_folder: Path) -> None:
    logger.info("Installing audio files...")
    for archive in media_archives:
        sounds_url = media_base_url + "sounds/" + archive
        zip_file = download_bin(sounds_url, media_folder)
        unzip(zip_file, media_folder, remove_zip=True)


def install_image(media_folder: Path) -> None:
    logger.info("Installing image file...")
    image_url = media_base_url + "images/Age_of_Empires_2_Logo.png"
    image_file = download_bin(image_url, media_folder)
    logger.info(f"Image file {image_file} installed")


def bootstrap() -> None:
    media_folder = create_media_folder()

    if check_bootstrap(media_folder):
        logger.info("Audio files already installed")
        return

    install_sounds(media_folder)
    install_image(media_folder)

    finish_bootstrap(media_folder)
