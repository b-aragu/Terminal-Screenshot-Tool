#usr/bin/env python3
import os
import subprocess
import tempfile

def capture_terminal_screenshot(output_path, format="PNG"):
    """
    Capture a screenshot of the active terminal window.

    :param output_path: Path to save the captured screenshot.
    :param format: Output format (default is PNG).
    """
    try:
        terminal_window_id = int(subprocess.getoutput("xdotool getactivewindow"))
        
        # Create a temporary XWD file
        with tempfile.NamedTemporaryFile(suffix=".xwd", delete=False) as temp_xwd_file:
            temp_xwd_path = temp_xwd_file.name
        
        # Capture the screenshot using xwd
        subprocess.run(["xwd", "-id", str(terminal_window_id), "-out", temp_xwd_path])
        
        # Convert the temporary XWD file to the specified format
        subprocess.run(["convert", temp_xwd_path, format + ":" + output_path])
        
        # Remove the temporary XWD file
        os.remove(temp_xwd_path)
    except Exception as e:
        print(f"Error capturing screenshot: {e}")

