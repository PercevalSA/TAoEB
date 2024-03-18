from pathlib import Path
from zipfile import ZipFile
import requests
import logging

media_base_url = (
    "https://media.githubusercontent.com/media/PercevalSA/TAoEB/main/assets/sounds/"
)
sounds_url_1 = media_base_url + "named.zip"
sounds_url_2 = media_base_url + "unnamed.zip"

logger = logging.getLogger(__name__)

def unzip(zip_file: Path, dest_folder: Path, *, remove_zip: bool = False):
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


def download_sounds(dest_folder: Path):
    download_zip(sounds_url_1, dest_folder)
    download_zip(sounds_url_2, dest_folder)


def bootstrap_folder() -> Path:
    logger.info("Creating sounds folder if missing")
    sounds_folder = Path(__file__).parent / "sounds"
    sounds_folder.mkdir(exist_ok=True)
    return sounds_folder


def install_sounds():
    sounds_folder = bootstrap_folder()
    download_sounds(sounds_folder)
    unzip(sounds_folder / "named.zip", sounds_folder, remove_zip=True)