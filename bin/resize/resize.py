#!/usr/bin/env python3

import argparse
import sys
from PIL import Image
import io

def resize_image(input_stream, output_stream, width, height, keep_aspect):
    with Image.open(input_stream) as img:
        orig_width, orig_height = img.size

        # If no resizing is needed, just copy
        if width is None and height is None:
            img.save(output_stream, format="PNG", optimize=True)
            return

        # If only one is provided, handle aspect ratio
        if keep_aspect:
            if width and not height:
                height = int((width / orig_width) * orig_height)
            elif height and not width:
                width = int((height / orig_height) * orig_width)
        elif width is None or height is None:
            raise ValueError(
                "If only one of --width or --height is provided, you must also pass --keep-aspect-ratio"
            )

        resized = img.resize((width, height), Image.LANCZOS)
        resized.save(output_stream, format="PNG", optimize=True)

def main():
    parser = argparse.ArgumentParser(
        description="📐 Resize an image to the target width and/or height. "
                    "Use --keep-aspect-ratio to infer missing dimension."
    )
    parser.add_argument('--in', dest='input_path', default='-', help="Input image path or '-' for stdin (default: -)")
    parser.add_argument('--out', dest='output_path', default='-', help="Output image path or '-' for stdout (default: -)")
    parser.add_argument('--width', type=int, help="Target width (pixels)")
    parser.add_argument('--height', type=int, help="Target height (pixels)")
    parser.add_argument('--keep-aspect-ratio', action='store_true', help="Preserve aspect ratio if only one dimension is given")

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

    resize_image(input_stream, output_stream, args.width, args.height, args.keep_aspect_ratio)

if __name__ == "__main__":
    main()

