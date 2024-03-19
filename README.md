# aoe2-bot

Age Of Empires II Telegram Bot: give a random quote of Age of Empires 2 original edition

available [here](https://web.telegram.org/k/#@age_of_empires_2_bot)

## Installation

Get the service file from github repository and set an environment file with your telegram bot token as `TGB_TOKEN`
```
git clone https://github.com/PercevalSA/aoe2-bot
cd aoe2-bot
python3 -m pip install .
mkdir -p $HOME/.config/aoe2-bot
echo 'TGB_TOKEN=xxxx' >$HOME/.config/aoe2-bot/env
```

## Installed sounds

 * `taunt.zip` are french taunt in `mp3` format. There are 42 taunts in total.
    * their name are composed of a 2 padded number (like 02 or 15), a space and the name
 * `civilization.zip` are all specific civilization start sounds in `mp3` format
    * their name is a single word starting with a capital letter
 * `sound.zip` are all in game sounds (building, generic units...) in `wav` format
    * their name is full lowercase and can have a number only at the end (e.g. multiples sounds for the same thing)


## How to get sounds
to get sound checks your steam files in `$HOME/.steam/steam/steamapps/common/AoE2DE/wwise/` and get `pck` files.

Get the softwares

You need to extract .pck that contains .bnk files that contain wem files that you need to convert to wav or ogg.

 * [extract pck](https://www.scampers.org/steve/sms/other.htm#ravioli_download) but is windows only
 * [extract bnk](https://github.com/hcs64/vgm_ripping) or [this updated one](https://github.com/eXpl0it3r/bnkextr/tree/master)
 * [convert ww to ogg](https://github.com/hcs64/ww2ogg)


If you build `wwisexmabank` or `xmash` on mondern Linux add `  $(CC) $^ -o $@ $(LDFLAGS)` on line 10 in `Makefile.common`
