#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import time

def add_timestamp(input_path, output_path, format="PNG"):
    """
    Add a timestamp to an image.

    :param input_path: Path to the input image.
    :param output_path: Path to save the modified image.
    :param format: Output format (default is PNG).
    """
    try:
        # Wait for the file to be fully written to the disk
        time.sleep(1)

        image = Image.open(input_path)

        # Add a timestamp to the image
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        draw.text((10, 10), timestamp, (255, 255, 255), font=font)

        image.save(output_path, format=format)
    except Exception as e:
        print(f"Error adding timestamp to the image: {e}")

