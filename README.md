# TAoEB
Telegram Age Of Empires II Bot: give a random quote of Age of Empires 2 original edition

# How to get sounds
to get sound checks your steam files in `$HOME/.steam/steam/steamapps/common/AoE2DE/wwise/` and get `pck` files.

Get the softwares

You need to extract .pck that contains .bnk files that contain wem files that you need to convert to wav or ogg.

 * [extract pck](https://www.scampers.org/steve/sms/other.htm#ravioli_download) but is windows only
 * [extract bnk](https://github.com/hcs64/vgm_ripping) or [this updated one](https://github.com/eXpl0it3r/bnkextr/tree/master)
 * [convert ww to ogg](https://github.com/hcs64/ww2ogg)


If you build `wwisexmabank` or `xmash` on mondern Linux add `  $(CC) $^ -o $@ $(LDFLAGS)` on line 10 in `Makefile.common`