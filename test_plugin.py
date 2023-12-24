PLUGIN_METADATA = {
    'name': 'Uppercase Converter',
    'version': '1.0',
    'author': 'Camille.Is_Me',
    'description': 'Converts given string to uppercase. A template plugin to help user understand plugins.',
}

def info():
    """
    Returns information about the plugin.
    """
    return PLUGIN_METADATA

def register_args(parser):
    """
    Register arguments for the uppercase plugin.
    """
    parser.add_argument('--uppercase', type=str, help='Convert this string to uppercase')

def execute(args):
    """
    Execute the uppercase conversion.
    """
    if args.uppercase:
        print(args.uppercase.upper())
