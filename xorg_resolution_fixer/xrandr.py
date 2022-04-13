import os


def run(cmd):
    return os.popen(cmd).read()


def getDisplays():
    display_str = run('xrandr -q | grep " connected"')
    display_lst = []

    for line in display_str.split('\n'):
        line = line.split(' ')[0]
        if line != '':
            display_lst.append(line.split(' ')[0])

    return display_lst


def getDisplayOrExitIfNone(display):
    display_lst = getDisplays()

    if (len(display_lst) == 0):
        print('Man, it looks like you don\'t have any display. WTF')
        exit(1)

    if display is None:
        display = display_lst[0]
    
    elif display not in display_lst:
        print('[WARNING] The passed display is not recognized by xrandr. Hoping you know what you\'re doing.\n')

    return display


def fixResolution(height, width, refresh_rate, display):
    display_str = run('xrandr -q | grep " connected"')
    
    display = getDisplayOrExitIfNone(display)

    print(f'Setting up display {display} with resolution {width}x{height} and refresh rate {refresh_rate}')

    out = run(f'cvt {width} {height} {refresh_rate}').split(' ')
    
    name = out[12][:-1][1:];
    modeline_str = f"\"{name}\" {' '.join(out[-14:])}";

    run(f'xrandr --newmode {modeline_str}')
    run(f'xrandr --addmode {display} {name}')
