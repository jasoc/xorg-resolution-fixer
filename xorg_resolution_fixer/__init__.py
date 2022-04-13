import getpass
import argparse

from .xrandr import fixResolution, getDisplayOrExitIfNone
from .systemd import createService


def main():
    parser = argparse.ArgumentParser(description="Backup script for VMware ESXi")

    parser.add_argument("-e", "--height", type=int, nargs='?',
                        default=1080, help="Height of the resolution")
    
    parser.add_argument("-w", "--width", type=int, nargs='?',
                        default=1920, help="Width of the resolution")
    
    parser.add_argument("-r", "--refresh-rate", type=int, nargs='?',
                        default=60, help="Refresh rate of the resolution")

    parser.add_argument("-d", "--display", type=str,
                        help="Display to be used")

    parser.add_argument("-u", "--user", type=str,
                        help="User that start the X server. Needed for systemd installation")

    parser.add_argument('-s', '--set', dest='set',
                        nargs='?', const=True, default=False,
                        help='Execute the script without')

    parser.add_argument('-i', '--install', dest='install',
                        nargs='?', const=True, default=False,
                        help='Create a systemd service that call the script after display-manager.service')

    args = parser.parse_args()

    user = args.user if args.user is not None else getpass.getuser()

    display = getDisplayOrExitIfNone(args.display)

    if args.set:
        fixResolution(args.height, args.width, args.refresh_rate, display)
    elif args.install:
        createService(args.height, args.width, args.refresh_rate, display, user)
    else:
        parser.print_help()