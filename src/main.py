#!/usr/bin/env python3
import os
import time
import argparse
from setup_configuration import setup_configuration
from capture_screenshot import capture_terminal_screenshot
from image_processing import add_timestamp
import logging

# Define the log file path
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__ + "/..")), "logs")
log_file = os.path.join(log_dir, "screenshot.log")

# Ensure the log directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Initialize the logging system with append mode
logging.basicConfig(filename=log_file, level=logging.INFO, filemode="a")

def main():
    parser = argparse.ArgumentParser(description="Capture and process screenshots")
    parser.add_argument("--output-dir", default=None, help="Output directory for screenshots")
    args = parser.parse_args()

    # Run the interactive setup if --output-dir is not specified
    if args.output_dir is None:
        output_dir = setup_configuration()
  # comment debuggin info      print(f"output_dir: {output_dir}")
    else:
        output_dir = args.output_dir

    try:
        timestamp = time.strftime("%Y%m%d%H%M%S", time.gmtime())
        output_filename = f"screenshot_{timestamp}.png"
    # comment debuggin info    print(f"output_filename: {output_filename}")
        screenshot_path = os.path.join(output_dir, output_filename)
        capture_terminal_screenshot(screenshot_path)
        add_timestamp(screenshot_path, screenshot_path)
        logging.info(f"Screenshot captured and timestamp added to: {screenshot_path}")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()

