import os
from .xrandr import run

xrf_service_name = 'xorg-resolution-fixer.service'


def defaultSystemdPath(user):
    return f'/home/{user}/.config/systemd/user'


def getService(height, width, refresh_rate, display, xrf_path):
    return f'''
[Unit]
Description=Xorg resolution fixer
BindsTo=graphical-session.target
After=graphical-session.service

[Service]
Type=simple
ExecStart={xrf_path} -s -e {height} -w {width} -r {refresh_rate} -d {display}

[Install]
WantedBy=graphical-session.target
'''


def createService(height, width, refresh_rate, display, user):
    xrf_path = '/usr/local/bin/xrf'
    if not os.path.isfile(xrf_path):
        xrf_path = '/usr/bin/xrf'
        if not os.path.isfile(xrf_path):
            print("[ERROR] xrf binary not found in /usr/local/bin/xrf or /usr/bin/xrf. Cannot create systemd service.")
            exit(1)
    os.makedirs(defaultSystemdPath(user), exist_ok=True)
    with open(f'{defaultSystemdPath(user)}/{xrf_service_name}', 'w') as f:
        f.write(getService(height, width, refresh_rate, display, xrf_path))
    run("systemctl --user daemon-reload")
    run(f"systemctl --user enable --now {xrf_service_name}")
