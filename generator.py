#!/usr/bin/env python3

import argparse
import sys

PADDING_CHAR = '_'


def parse_args(args):
    parser = argparse.ArgumentParser(args)

    parser.add_argument(
        '--primary-color'
    )

    parser.add_argument(
        '--secondary-color'
    )

    parser.add_argument(
        '--key-padding',
        type=int,
        default=0
    )

    parser.add_argument(
        '--value-padding',
        type=int,
        default=0
    )

    parser.add_argument(
        'text',
        nargs='+'
    )

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    output = f'%{{F{args.primary_color}}}%{{B{args.primary_color}}}'

    for text in args.text:
        key, value = text.split(':')

        if text == args.text[len(args.text) - 1]:
            # last loop
            output += f'%{{F{args.primary_color}}}{PADDING_CHAR * args.key_padding}%{{F-}}{key}%{{F{args.primary_color}}}{PADDING_CHAR * args.key_padding}%{{B{args.secondary_color}}}%{{F{args.secondary_color}}}{PADDING_CHAR * args.value_padding}%{{F-}}{value}%{{F{args.secondary_color}}}{PADDING_CHAR * args.value_padding}%{{B-}}'
        else:
            output += f'%{{F{args.primary_color}}}{PADDING_CHAR * args.key_padding}%{{F-}}{key}%{{F{args.primary_color}}}{PADDING_CHAR * args.key_padding}%{{B{args.secondary_color}}}%{{F{args.secondary_color}}}{PADDING_CHAR * args.value_padding}%{{F-}}{value}%{{F{args.secondary_color}}}{PADDING_CHAR * args.value_padding}%{{B{args.primary_color}}}'

    print(output)


if __name__ == '__main__':
    main()
