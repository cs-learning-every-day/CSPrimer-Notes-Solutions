"""
CSS Color Convert Plan:

    1. Define function to convert hexadecimal to RGB values
        i.e. hex_to_rgb('#00ff00') == 'rgb(0, 255, 0)'
    2. Write a main function that takes some text, applies regex to the text and applies the funciton

"""
import sys
import re

HEX_RGB_MAP = {
    '#000000': 'rgb(0 0 0)',
    '#000001': 'rgb(0 0 1)',
    '#ff0000': 'rgb(255 0 0)',
    '#ffffff': 'rgb(255 255 255)',
    '#123': 'rgb(17 34 51)',
    '#fff': 'rgb(255 255 255)',
    '#0000FFC0': 'rgba(0 0 255 / 0.75294)',
    '#00f8': 'rgba(0 0 255 / 0.53333)'
}


def hex_to_rgb(hex: str) -> str:
    if hex[0] == '#':
        hex = hex[1:]
    rgb_vals = []
    hex_len = len(hex)
    if hex_len in (3,4):
        idx = 1
    else:
        idx = 2
    while hex:
        hex_part = hex[:idx]
        if len(rgb_vals) == 3:
            conversion = alpha_convert(hex_part)
        else:
            conversion = rgb_convert(hex_part)
        #conversion = int(hex[:idx], 16) * 17**conversion_factor
        rgb_vals.append(conversion)
        hex = hex[idx:]
    if len(rgb_vals) == 4:
        return f'rgba({rgb_vals[0]} {rgb_vals[1]} {rgb_vals[2]} / {rgb_vals[3]:.5f})'
    return f'rgb({rgb_vals[0]} {rgb_vals[1]} {rgb_vals[2]})'
    

def rgb_convert(hex: str) -> int:
    if len(hex) == 2:
        return int(hex, 16)
    return int(hex, 16) * 17


def alpha_convert(hex: str) -> int:
    return rgb_convert(hex) / 255


def process_text(line: str) -> None:
    hex_match = r'#[A-Fa-f0-9]{3,8}'
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
    if len(sys.argv) > 1 and sys.argv[1] == '-c':
        convert()
    else:
        main()
