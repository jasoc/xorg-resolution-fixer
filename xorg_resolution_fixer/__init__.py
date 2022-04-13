import getpass
import argparse

from .xrandr import fixResolution, getDisplayOrExitIfNone, getDisplays
from .systemd import createService


def main():
    parser = argparse.ArgumentParser(description="Xorg resolution fixer")

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

    parser.add_argument('-l', '--list-displays', dest='list_displays',
                        nargs='?', const=True, default=False,
                        help='List the available displays')

    args = parser.parse_args()

    user = args.user if args.user is not None else getpass.getuser()
    display = getDisplayOrExitIfNone(args.display)
    nop = True

    if args.set:
        fixResolution(args.height, args.width, args.refresh_rate, display)
        nop = False
    if args.install:
        createService(args.height, args.width,
                      args.refresh_rate, display, user)
        nop = False
    if args.list_displays:
        for d in getDisplays():
            print(d)
        nop = False
    if nop:
        parser.print_help()
