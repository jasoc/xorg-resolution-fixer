
#  Xorg resolution fixer

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

##  What is ___Xorg resolution fixer___?
It is a python module that uses ___xrandr___ and ___cvt___ to force a specific resolution whenever a supported resolution doesn't appear in your monitor settings. For instance, it determines the VESA CVT modelines with the command ```cvt {width}  {height}  {refresh_rate}``` and passes it to xrandr by calling ```xrandr --newmode {modeline_str}``` and ```xrandr --addmode {display} {name}``` 

---

## What is the advantage?
It automates the above procedure simply by calling

```bash
xrf --set --height 1080 --width 1920 --refresh-rate 120
```

plus, with the ```--install``` parameter it can configure a systemd service that call the command at every boot.

---

## How to use it

To install **xrf** in your system, issue the following commands:

```bash
git clone https://github.com/jasoc/xorg-resolution-fixer.git

cd xorg-resolution-fixer

sudo python setup.py install
```

Then you will have the **xrf** command globally available in your system.
To fix a resolution, this is the magic line:

```bash
xrf --set --height 1080 --width 1920 --refresh-rate 120 --display HDMI-1
```

Be aware that the ```--display``` parameter requires any available display that you can list with

```
xrf --list-display
```

To install it as a systemd service, use


```bash
xrf --install --height 1080 --width 1920 --refresh-rate 120 --user boblazar
```
```bash
systemctl --user enable --now xorg-resolution-fixer
```

The ```--user``` parameter should be the user that runs the X server at the boot. Most of the time is your standard user, so if you don't specify, that will be used. Just be aware of that if you have any kind of special configuration of Xorg.

Anyway, a detailed list of command is available with

```bash
xrf --help
```

---

## Why
Well, for some misterious reasons, with some monitor (expecially TVs) some resolutions doesn't appear under Xorg, even if supported. But, for the same misterious reasons, you can force it! What a deal! This module helps you doing so.
If you wonder, it all began when I decided to switch from Gnome under Wayland to Gnome under Xorg, since Wayland isn't supported pretty much by anything, and seeing my old-fashion TV I am using as a monitor in a totally broken resolution made me nuts.

---

## License
### [MIT](LICENSE)

---

## Contributing
You are free to reuse and contribute to the project, I'll eventually accept the pull requests if the proposed features fits the initial aim of the project.
