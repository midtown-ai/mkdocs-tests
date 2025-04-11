#!/usr/bin/env python3

import argparse
import sys
from PIL import Image
import io

def crop_image(input_stream, output_stream, x, y, width, height, x_align, y_align):
    with Image.open(input_stream) as img:
        img_width, img_height = img.size

        # Default crop size to full image (minus offset)
        w = width if width is not None else img_width - (x if x is not None else 0)
        h = height if height is not None else img_height - (y if y is not None else 0)

        # Compute x if not provided
        if x is None:
            if x_align == 'left':
                x = 0
            elif x_align == 'middle':
                x = (img_width - w) // 2
            elif x_align == 'right':
                x = img_width - w
        # Compute y if not provided
        if y is None:
            if y_align == 'top':
                y = 0
            elif y_align == 'middle':
                y = (img_height - h) // 2
            elif y_align == 'bottom':
                y = img_height - h

        # Validate crop box
        if x < 0 or y < 0 or x + w > img_width or y + h > img_height:
            raise ValueError(f"Crop area ({x},{y},{w},{h}) exceeds image bounds ({img_width}x{img_height})")

        cropped = img.crop((x, y, x + w, y + h))
        cropped.save(output_stream, format="PNG", optimize=True)

def main():
    parser = argparse.ArgumentParser(description="Crop an image to a given box with optional alignment.")
    parser.add_argument('--in', dest='input_path', default='-', help="Input file path or '-' for stdin")
    parser.add_argument('--out', dest='output_path', default='-', help="Output file path or '-' for stdout")
    parser.add_argument('--x', type=int, help="X coordinate of top-left corner (overrides x-align)")
    parser.add_argument('--y', type=int, help="Y coordinate of top-left corner (overrides y-align)")
    parser.add_argument('--width', type=int, help="Width of crop area (default: image width - x)")
    parser.add_argument('--height', type=int, help="Height of crop area (default: image height - y)")
    parser.add_argument('--crop-x-align', choices=['left', 'middle', 'right'], default='left',
                        help="Horizontal alignment if x not specified (default: left)")
    parser.add_argument('--crop-y-align', choices=['top', 'middle', 'bottom'], default='top',
                        help="Vertical alignment if y not specified (default: top)")

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

    crop_image(
        input_stream,
        output_stream,
        x=args.x,
        y=args.y,
        width=args.width,
        height=args.height,
        x_align=args.crop_x_align,
        y_align=args.crop_y_align
    )

if __name__ == "__main__":
    main()
