import os

def setup_configuration():
    # Get the script's directory path
    script_dir = os.path.dirname(os.path.abspath(__file__ + "/.."))

    print("Welcome to the Screenshot Directory Setup Script!")
    user_input = input("Enter the directory where you want to store the screenshots, or press Enter to use the default 'screenshots' directory: ")

    if user_input:
        # Use the user-specified directory
        output_dir = os.path.join(script_dir, user_input)
    else:
        # Use the default 'screenshots' directory
        output_dir = os.path.join(script_dir, "screenshots")

    # Create the screenshot directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Screenshot directory set up at: {output_dir}")
    return output_dir

if __name__ == "__main__":
    setup_configuration()

