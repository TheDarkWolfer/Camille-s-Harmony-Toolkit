PLUGIN_METADATA = {
    'name': 'Asymetric Encryption (RSA)',
    'version': '1.0',
    'author': 'Camille.Is_Me',
    'description': 'A plugin to handle asymetric encryption, using 2048-bit (or higher) RSA keys',
    'dependencies' : ['cryptography'] #Fill out with your plugin's dependencies
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
    parser.add_argument('--rsa', type=str, help="Generate a RSA key pair and save both under <keyname>.pri and <keyname>.pub")
    parser.add_argument('--rsa-encrypt',type=str,help="Use public key <keyname> to encrypt a given string (needs to be used with --rsa-key)")
    parser.add_argument('--rsa-decrypt',type=str,help="Use private key <keyname> to decrypt a given string (needs to be used with --rsa-key)")
    parser.add_argument('--rsa-key',type=str,help="RSA key to use (public or private, dependant on the other arguments used)")
    parser.add_argument('--keysize',type=int,help="Use a different RSA key size (in bits)(processing power required scales with key size)")

def execute(args,DOWNLOAD_DIR,DATA_DIR,doForce):
    """
    Execute the whole plugin.
    """

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes

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

    KEYSIZE = 2048

    def generate_key_pair():
        """
        Generate a new RSA public/private key pair and return them.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=KEYSIZE,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def save_private_key_to_file(private_key, filename):
        """
        Save an RSA private key to a file.
        """
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(filename, "wb") as key_file:
            key_file.write(pem)

    def save_public_key_to_file(public_key, filename):
        """
        Save an RSA public key to a file.
        """
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(filename, "wb") as key_file:
            key_file.write(pem)

    def load_private_key_from_file(filename):
        """
        Load an RSA private key from a file.
        """
        with open(filename, "rb") as key_file:
            pem = key_file.read()
        private_key = serialization.load_pem_private_key(
            pem,
            password=None,
            backend=default_backend()
        )
        return private_key

    def load_public_key_from_file(filename):
        """
        Load an RSA public key from a file.
        """
        with open(filename, "rb") as key_file:
            pem = key_file.read()
        public_key = serialization.load_pem_public_key(
            pem,
            backend=default_backend()
        )
        return public_key

    def encrypt_string(message, public_key):
        """
        Encrypt a string using the provided RSA public key.
        """
        encrypted_message = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt_string(encrypted_message, private_key):
        """
        Decrypt an encrypted string using the provided RSA private key.
        """
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()
        return decrypted_message

    def is_power_of_two(n):
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    def round_to_nearest_power_of_two(n):
        if n < 1:
            raise ValueError("Number must be greater than 0")
        # Find the closest power of two greater than or equal to n
        power = 1
        while power < n:
            power *= 2
        # Check if n is closer to the previous or the current power of two
        previous_power = power // 2
        if n - previous_power < power - n:
            return previous_power
        else:
            return power



    if args.keysize:
        if not is_power_of_two(args.keysize) and not doForce:
            print(f"[{RED}!{RESET}] The key size is not a power of 2. There may be issues due to this !")
            print(f"[{GOLD}i{RESET}] Use -f to override this")
            exit(1)
        elif not is_power_of_two(args.keysize) and doForce:
            print(f"[{RED}!{RESET}] The key size is not a power of 2. There may be issues due to this !")
            print(f"[{GOLD}i{RESET}] User override, proceeding...")
        
        KEYSIZE = args.keysize

    if args.rsa:

        print(f"[{GREEN}+{RESET}] Generating keypair...")
        private, public = generate_key_pair()

        print(f"[{GREEN}+{RESET}] Saving private key {GOLD}{args.rsa}.pri{RESET}")
        save_private_key_to_file(private,f"{args.rsa}.pri")

        print(f"[{GREEN}+{RESET}] Saving public key {GOLD}{args.rsa}.pub{RESET}")
        save_public_key_to_file(public,f"{args.rsa}.pub")

    if args.rsa_encrypt:
        if args.rsa_key:
            public = load_public_key_from_file(f"{args.rsa_key}")

            encrypted_string = encrypt_string(args.rsa_encrypt,public)
            print(f"[{CYAN}*{RESET}] Operation done !")
            print(f"[{GOLD}i{RESET}] Original text  : {args.rsa_encrypt}")
            print(f"[{GOLD}i{RESET}] Encrypted text : {encrypted_string}")
            exit(0)
        
        else:
            print(f"[!] You need to provide a valid RSA key !")
            exit(1)

    if args.rsa_decrypt:
        if args.rsa_key:
            private = load_private_key_from_file(f"{args.rsa_key}")

            decrypted_string = decrypt_string(args.rsa_encrypt,args.rsa)
            print(f"[{CYAN}*{RESET}] Operation done !")
            print(f"[{GOLD}i{RESET}] Original text  : {args.rsa_decrypt}")
            print(f"[{GOLD}i{RESET}] Decrypted text : {decrypted_string}")
            exit(0)
        
        else:
            print(f"[!] You need to provide a valid RSA key !")
            exit(1)