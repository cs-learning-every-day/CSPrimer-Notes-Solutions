"""
CSS Color Convert Plan:

    1. Define function to convert hexadecimal to RGB values
        i.e. hex_to_rgb('#00ff00') == 'rgb(0, 255, 0)'
    2. Write a main function that takes some text, applies regex to the text and applies the funciton

"""
import sys
import re

HEX_RGB_MAP = {
    '#000000': 'rgb(0, 0, 0)',
    '#000001': 'rgb(0, 0, 1)',
    '#ff0000': 'rgb(255, 0, 0)',
    '#ffffff': 'rgb(255, 255, 255)'
}


def hex_to_rgb(hex: str) -> str:
    if hex[0] == '#':
        hex = hex[1:]
    rgb_vals = []
    while hex:
        rgb_vals.append(int(hex[:2], 16))
        hex = hex[2:]
    return f'rgb({rgb_vals[0]} {rgb_vals[1]} {rgb_vals[2]})'


def process_text(line: str) -> None:
    hex_match = r'#[A-Fa-f0-9]{6}'
    matches = re.findall(hex_match, line)
    if not matches:
        sys.stdout.write(line)
        return
    for match in matches:
        line = line.replace(match, hex_to_rgb(match))
    sys.stdout.write(line)



def main():
    for hex, rgb in HEX_RGB_MAP.items():
        res = hex_to_rgb(hex)
        assert res == rgb, f'\nhex: {hex}\nrgb: {rgb}\nres: {res}'
    print('COMPLETED!')


def convert():
    for line in sys.stdin:
        process_text(line)


if __name__ == '__main__':
    convert()
