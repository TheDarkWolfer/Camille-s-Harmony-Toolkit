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

To install Harmony Toolkit, follow these steps:

Clone from the repository :
`git clone https://TheDarkWolfer/Camille-s-Harmony-Toolkit/`

Navigate to the new directory :
`cd /Camille-s-Harmony-Toolkit`

Ensure you have all the requirements installed :
`pip install -r requirements.txt`

## Usage

To use Harmony Toolkit, open your terminal or command prompt and navigate to the directory where the toolkit is located. You can perform various operations as follows:
You can also add a shorter alias to use the tool by running this command:

`echo "alias cht='harmonytoolkit'" >> ~/.zshrc | ~/.bashrc #Choose depending on the shell you use`

Or copy the main file (harmonytoolkit <- Python File) to your /usr/bin 
(Just make sure you give it the right permissions to avoid opening gaping holes into your network security)
`cp <wherever you have the dir>/Camille-s-Harmony-Toolkit/harmonytoolkit /usr/bin/`



Usage :

`harmonytoolkit [options] [input]`

Examples

    Convert Binary to ASCII:

`harmonytoolkit -b2a 01001000`

Encrypt a File:

`harmonytoolkit -e myfile.txt keyfile`

Generate a QR Code:

`harmonytoolkit -qr "Sample Text"`

Refer to the provided help page for a complete list of options and their descriptions.


# Plugins : 

You can write plugins to add to the tool without having to mess with the main file, by writing a small python script
following simple guidelines and placing it in /home/.harmonytoolkit/plugins/

You can find the template plugin in this repository, so you can easily copy, paste and modify it. Just make sure to respect
the established structure, else the program won't like your plugin and throw a hissy fit.

To list plugins, you can use this command :
`harmonytoolkit -pl`

To see more information about a plugin, use this command :
`harmonytoolkit -pi <plugin name>`

Have fun with it, and don't hesitate to share your plugin with others <3
(Just make sure the plugins you use do not contain malicious code, be safe out there)
