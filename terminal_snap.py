import os
from PIL import Image, ImageDraw, ImageFont
import subprocess
import time
import tempfile

# Get the script's directory path
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "screenshots")

# Define the default file name and screenshot format
output_filename = "screenshot.png"
default_format = "PNG"

# Define the interval (in seconds) between automatic screenshots
screenshot_interval = 10

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Capture a screenshot of the terminal
def capture_terminal_screenshot(output_path, format="PNG"):
    terminal_window_id = int(subprocess.getoutput("xdotool getactivewindow"))
    
    # Create a temporary XWD file
    with tempfile.NamedTemporaryFile(suffix=".xwd", delete=False) as temp_xwd_file:
        temp_xwd_path = temp_xwd_file.name
    
    # Capture the screenshot using xwd
    subprocess.run(["xwd", "-id", str(terminal_window_id), "-out", temp_xwd_path])
    
    # Convert the temporary XWD file to PNG
    subprocess.run(["convert", temp_xwd_path, format + ":" + output_path])
    
    # Remove the temporary XWD file
    os.remove(temp_xwd_path)
# Modify the captured screenshot
def modify_screenshot(input_path, output_path, format=default_format):
    # Wait for the file to be fully written to the disk
    time.sleep(1)

    image = Image.open(input_path)
    
    # Add a timestamp to the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    draw.text((10, 10), timestamp, (255, 255, 255), font=font)

    image.save(output_path, format=format)

# Take automatic screenshots at a specified interval
def auto_capture_screenshots(interval, format=default_format):
    while True:
        timestamp = time.strftime("%Y%m%d%H%M%S", time.gmtime())
        screenshot_path = os.path.join(output_dir, f"screenshot_{timestamp}.{format}")
        capture_terminal_screenshot(screenshot_path)
        modify_screenshot(screenshot_path, screenshot_path, format=format)
        time.sleep(interval)

# Main function
def main():
    # Capture a single screenshot
    screenshot_path = os.path.join(output_dir, output_filename)
    capture_terminal_screenshot(screenshot_path)

    # Uncomment the following line to enable automatic screenshot capture
    # auto_capture_screenshots(screenshot_interval, format=default_format)

if __name__ == "__main__":
    main()


