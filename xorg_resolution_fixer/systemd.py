import os


xrf_service_name = 'xorg-resolution-fixer.service'


def defaultSystemdPath(user):
    return f'/home/{user}/.config/systemd/user'


def getService(height, width, refresh_rate, display):
    return f'''
[Unit]
Description=Xorg resolution fixer
BindsTo=graphical-session.target
After=graphical-session.service

[Service]
Type=simple
ExecStart=/usr/bin/xrf -s -e {height} -w {width} -r {refresh_rate} -d {display}

[Install]
WantedBy=graphical-session.target
'''


def createService(height, width, refresh_rate, display, user):
    with open(f'{defaultSystemdPath(user)}/{xrf_service_name}', 'w') as f:
        os.makedirs(defaultSystemdPath(user), exist_ok=True)
        f.write(getService(height, width, refresh_rate, display))
