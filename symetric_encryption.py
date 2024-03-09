PLUGIN_METADATA = {
    'name': 'Symetric Encryption (AES)',
    'version': '1.0',
    'author': 'Camille.Is_Me',
    'description': 'A plugin to handle symetric encryption, AES keys',
    'dependencies' : ['cryptography','os'] #Fill out with your plugin's dependencies
}

def info():
    """
    Returns information about the plugin. Better not touch this function, as
    it is used to provide information about this plugin to the main program, and
    tampering with this function might cause issues.

    Have fun <3
    """
    return PLUGIN_METADATA

def register_args(parser):
    """
    Register arguments for the plugin.
    """

    #Here we register all the arguments our plugin needs to function.
    
    RESET = '\033[0m'
    BOLD = '\033[1m'
    CRIMSON = '\033[38;5;196m'

    parser.add_argument("--aes-encrypt", type=str, help=f"\t[{CRIMSON}{BOLD}◼{RESET}] Encrypts the input file with AES-128. Used like so : --aes-encrypt <file>{BOLD}{CRIMSON}Use with caution{RESET}.")
    parser.add_argument("--aes-decrypt", type=str, help=f"\t[{CRIMSON}{BOLD}◼{RESET}] Decrypts the input file with AES-128. Used like so : --aes-decrypt <file>{BOLD}{CRIMSON}Use with caution{RESET}.")
    parser.add_argument("--aes-keygen", help=f"\t[{CRIMSON}{BOLD}◼{RESET}] Generates a new AES-128 key and saves it to a file. Used like so : --aes-keygen <keyfile>{BOLD}{CRIMSON}Use with caution{RESET}.")
    parser.add_argument("--aes-key", help=f"\t[{CRIMSON}{BOLD}◼{RESET}] AES-128 key to use. Used like so : --aes-key <keyfile>")


def execute(args,DOWNLOAD_DIR,DATA_DIR,doForce):
    """
    Execute the whole plugin.
    """

    from cryptography.fernet import Fernet
    import os

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    GOLD = '\033[38;5;214m'
    WHITE = '\033[37m'
    ORANGE = '\033[38;5;208m'
    CRIMSON = '\033[38;5;196m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    BLINK = '\033[5m'

    def correct_base64_padding(key):
        # Check if key's length is a multiple of 4
        # If not, add '=' padding to make it a multiple of 4
        padding_needed = len(key) % 4
        if padding_needed:  # If padding_needed is not 0
            corrected_key = key + '=' * (4 - padding_needed)
            print(f"[{GOLD}i{RESET}] Incorrect key padding. Correcting...")
        else:
            corrected_key = key
        return corrected_key

    def generate_key():
        """
        Generate a new Fernet key and return it as a string.
        """
        key = Fernet.generate_key()
        return key

    def save_key_to_file(key, filename):
        """
        Save a Fernet key to a file.
        """
        with open(filename, "wb") as key_file:
            key_file.write(key)

    def load_key_from_file(filename):
        """
        Load a Fernet key from a file and return it as bytes.
        """
        with open(filename, "rb") as key_file:
            key = key_file.read()

        correct_base64_padding(key)

        return key

    def encrypt_string(message, key):
        """
        Encrypt a string using the provided Fernet key.
        """
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message

    def decrypt_string(encrypted_message, key):
        """
        Decrypt an encrypted string using the provided Fernet key.
        """
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        return decrypted_message

    def encrypt_file(filename, key):
        """
        Encrypt a file using the provided Fernet key.
        """
        fernet = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

    def decrypt_file(filename, key):
        """
        Decrypt a file using the provided Fernet key.
        """
        fernet = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
    
    if args.aes_keygen:
        if os.path.exists(args.aes_keygen):
            if str(input(f"[{CYAN}?{RESET}] Do you want to overwrite {GOLD}{args.aes_keygen}{RESET} ({GREEN}y{RESET}/{CRIMSON}n{RESET})")) == "n":
                exit(0)
        print(f"[{CYAN}i{RESET}] Saved to {GOLD}{args.aes_keygen}{RESET}")
        save_key_to_file(generate_key(),args.aes_keygen)
        exit(0)

    if not args.aes_key and (args.aes_encrypt or args.aes_decrypt):
        print(f"[{CRIMSON}!{RESET}] You didn't provide an AES key to use !")

    if args.aes_key:
        KEY = load_key_from_file(args.aes_key)

    if args.aes_encrypt:
        if os.path.isfile(args.aes_encrypt):
            if str(input(f"[{CYAN}?{RESET}] Encrypt file {GOLD}{args.aes_encrypt}{RESET} ? ({GREEN}y{RESET}/{CRIMSON}n{RESET})")) == "n":
                exit(0)
            encrypt_file(args.aes_encrypt,KEY)
            print(f"[{GREEN}*{RESET}] Encrypting {GOLD}{args.aes_encrypt}{RESET}...")
        else:
            print(f"[{GREEN}*{RESET}] Origial string   : {GOLD}{args.aes_encrypt}{RESET}")
            print(f"[{GREEN}*{RESET}] Encrypted string : {GOLD}{BOLD}{encrypt_string(args.aes_encrypt,KEY)}{RESET}")

    if args.aes_decrypt:
        if os.path.isfile(args.aes_decrypt):
            if str(input(f"[{CYAN}?{RESET}] Decrypt file {GOLD}{args.aes_decrypt}{RESET} ? ({GREEN}y{RESET}/{CRIMSON}n{RESET})")) == "n":
                exit(0)
            decrypt_file(args.aes_decrypt,KEY)
            print(f"[{GREEN}*{RESET}] Decrypting {GOLD}{args.aes_decrypt}{RESET}...")
        else:
            print(f"[{GREEN}*{RESET}] Origial string   : {GOLD}{args.aes_decrypt}{RESET}")
            print(f"[{GREEN}*{RESET}] Decrypted string : {GOLD}{BOLD}{decrypt_string(args.aes_decrypt,KEY)}{RESET}")
