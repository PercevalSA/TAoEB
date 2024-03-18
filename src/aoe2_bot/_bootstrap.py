from pathlib import Path
from zipfile import ZipFile
import requests

sounds_url_1 = "https://media.githubusercontent.com/media/PercevalSA/TAoEB/main/assets/sounds/named.zip"
sounds_url_2 = "https://media.githubusercontent.com/media/PercevalSA/TAoEB/main/assets/sounds/unnamed.zip"


def download_sounds(dest_folder: Path):
    download_zip(sounds_url_1, dest_folder)
    download_zip(sounds_url_2, dest_folder)


def unzip(zip_file: Path, dest_folder: Path, *, remove_zip: bool = False):
    with ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(dest_folder)
    if remove_zip:
        zip_file.unlink()


def download_zip(url: str, dest_folder: Path) -> Path:
    local_filename = url.split("/")[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


def install_sounds():
    print(__file__)
    download_sounds(Path(__file__).parent / "sounds")