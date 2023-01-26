import argparse
import pyautogui as p
from os import path
from subprocess import Popen


p.FAILSAFE = False  # https://pyautogui.readthedocs.io/en/latest/quickstart.html#fail-safes


def move_square(duration: float = 8.0, side_length: float = 64.0):
    side_duration = duration / 4
    p.moveRel(xOffset=side_length, yOffset=0, duration=side_duration)
    p.moveRel(xOffset=0, yOffset=side_length, duration=side_duration)
    p.moveRel(xOffset=(-side_length), yOffset=0, duration=side_duration)
    p.moveRel(xOffset=0, yOffset=(-side_length), duration=side_duration)


def main():
    parser = argparse.ArgumentParser(prog='Screen Activity Keeper',
                                     description='This program keeps your screen active and prevents auto lock',
                                     epilog='Run and go rest or take a shit.')
    parser.add_argument('-p', '--teams-path',
                        required=False,
                        dest='teams',
                        default=None,
                        metavar='MS Teams path',
                        help='Optional path to Microsoft Teams installation.')
    parser.add_argument('-m', '--mouse',
                        required=False,
                        action='store_true',
                        default=False,
                        help='Optional usage of mouse cursor.')

    args = parser.parse_args()

    while True:
        if args.teams:
            Popen(path.normpath(args.teams))
            # Re-opening the MS Teams many times won't create any new instances.
            # It will just focus on the currently open single instance of the program.
        if args.mouse:
            move_square()
        p.press("f18", presses=8, interval=0.5)
        p.sleep(300)


if __name__ == '__main__':
    main()
else:
    raise SystemExit(f'The "{__name__}" cannot be an imported module.')
