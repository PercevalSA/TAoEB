from pathlib import Path

current_module_folder = Path(__file__).parent
images_folder = current_module_folder / "images"
audio_caption = images_folder / "aok-ico.png"
audio_folder = current_module_folder / "audio"
bootstrap_file = audio_folder / "installation_complete"

audio_url = "https://media.githubusercontent.com/media/PercevalSA/aoe2-bot/main/audio"
audio_archives = [
    "civilization.zip",
    "sound.zip",
    "taunt.zip",
]
