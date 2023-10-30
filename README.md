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

- To capture a single screenshot of your active terminal window:

    ```shell
    python terminal.py
    ```

- To capture screenshots periodically at a specified interval (e.g., every 10 seconds):

    ```shell
    python terminal.py --interval 10
    ```

- To specify an output format (default is PNG):

    ```shell
    python terminal.py --format JPG
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

