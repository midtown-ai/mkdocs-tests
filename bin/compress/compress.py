#!/usr/bin/env python3

import argparse
import sys
from PIL import Image
import io

def compress_image(input_stream, output_stream, color_depth):
    if color_depth not in [2, 4, 8, 16, 32, 64]:
        raise ValueError("Color depth must be one of: 2, 4, 8, 16, 32, or 64")

    with Image.open(input_stream) as img:
        img_rgb = img.convert("RGB")
        quantized = img_rgb.quantize(colors=color_depth, method=Image.MEDIANCUT)
        quantized.save(output_stream, format="PNG", optimize=True)

def main():
    parser = argparse.ArgumentParser(
        description="📦 Compress a PNG by reducing its color depth. "
                    "Supports 2–64 colors. Works with file or stream I/O."
    )
    parser.add_argument(
        '--in', dest='input_path', default='-',
        help="Input PNG file path or '-' for stdin (default: -)"
    )
    parser.add_argument(
        '--out', dest='output_path', default='-',
        help="Output PNG file path or '-' for stdout (default: -)"
    )
    parser.add_argument(
        '--color-depth', dest='color_depth', type=int,
        choices=[2, 4, 8, 16, 32, 64], default=8,
        help="Target color depth (2, 4, 8, 16, 32, 64). Default: 8"
    )

    args = parser.parse_args()

    # Handle input
    if args.input_path == '-':
        input_stream = io.BytesIO(sys.stdin.buffer.read())
    else:
        input_stream = args.input_path

    # Handle output
    if args.output_path == '-':
        output_stream = sys.stdout.buffer
    else:
        output_stream = args.output_path

    compress_image(input_stream, output_stream, args.color_depth)

if __name__ == "__main__":
    main()

