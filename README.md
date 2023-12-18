# Introduction

Harmony Toolkit is a comprehensive collection of utilities designed for secure file management, data conversion, and encryption. Developed by Camille, this toolkit offers a range of features from secure file deletion to conversion between binary, hexadecimal, and ASCII, alongside robust encryption management tools.
Key Features

    ### Data Conversion: Convert data between binary, hex, and ASCII.
    ### File Security: Securely delete files with the nuke option.
    ### Encryption Tools: Manage file encryption and decryption using AES-128.
    ### Checksum Calculation: Compute MD5, SHA-256, and SHA-1 checksums for files.
    ### QR Code Generation: Create QR codes from text or file content.
    ### Output Customization: Options for colorful, kawaii, braille, and silly cipher outputs.
    ### Clipboard Integration: Copy outputs directly to the clipboard.
    ### Analysis Tool: Analyze input to determine its format.
    ### Version and Credits Display: Easily view toolkit version and credits.

# Installation

## To install Harmony Toolkit, follow these steps:

    Ensure you have Python installed on your machine.

    Download the Harmony Toolkit package from the provided source.

    Extract the package to your desired location.

    Open a terminal or command prompt.

    Navigate to the toolkit's directory.

    Run the following command to install any dependencies:

    `pip install -r requirements.txt`

## Usage

To use Harmony Toolkit, open your terminal or command prompt and navigate to the directory where the toolkit is located. You can perform various operations as follows:
You can also add a shorter alias to use the tool by running this command:

`echo "alias cht='harmonytoolkit'" >> ~/.zshrc | ~/.bashrc #Choose depending on the shell you use`

`harmonytoolkit [options] [input]`

Examples

    Convert Binary to ASCII:

`harmonytoolkit -b2a 01001000`

Encrypt a File:

`harmonytoolkit -e myfile.txt keyfile`

Generate a QR Code:

    `harmonytoolkit -qr "Sample Text"`

Refer to the provided help page for a complete list of options and their descriptions.
