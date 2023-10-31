# Terminal Screenshot Tool

The Terminal Screenshot Tool is a Python script that allows you to capture and modify screenshots of your terminal on Ubuntu and Debian-based systems. Whether you want to capture a single screenshot or set up automatic periodic captures, this tool has you covered.

## Features

- Capture screenshots of your active terminal window.
- Customize the output format (default is PNG).
- Automatically add a timestamp to each screenshot.
- Set up a periodic screenshot capture with a specified interval.
- Simple command-line interface for easy use.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Ubuntu or Debian-based Linux system.
- Python 3 installed.
- Required Python packages (`Pillow` for image manipulation).
- External tools: `xdotool` for capturing, and `convert` (from ImageMagick) for format conversion. These tools are pre-installed on many systems.

## Installation

1. Clone this repository to your local machine:

    ```shell
    git clone https://github.com/your-username/terminal-screenshot-tool.git
    ```

2. Install the required Python packages:

    ```shell
    pip install Pillow
    ```

## Usage

To use the Screenshot Capture and Processing script, you have two options for specifying the output directory:

1. **Interactive Setup:**
   - If you don't provide the `--output-dir` argument, the script will run an interactive setup where you can configure the output directory. Follow the prompts to select the directory or use the default 'screenshots' directory.

   Example:
   ```bash
   python main.py
    ```
2. Direct Directory Specification:

If you want to specify the output directory directly, provide the --output-dir argument followed by the directory path. This will skip the interactive setup.

    Example:
    ```bash 
    python main.py --output-dir /path/to/your/directory
    ```

## Configuration

You can configure the tool by editing the `config.json` file:

- `interval`: Set the screenshot interval in seconds.
- `format`: Set the default output format (e.g., PNG, JPG).

## Error Handling

The tool includes error handling to provide informative messages for common issues. If you encounter problems, check the error message for guidance.

## Contributing

Feel free to contribute to this project. You can open issues, submit pull requests, or suggest new features. Your input is valuable.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code.

---

Enjoy capturing and customizing your terminal screenshots with the Terminal Screenshot Tool!

