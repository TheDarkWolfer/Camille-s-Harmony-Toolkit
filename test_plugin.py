PLUGIN_METADATA = {
    'name': 'Uppercase Converter',
    'version': '1.0',
    'author': 'Camille.Is_Me',
    'description': 'A demo plugin to help users understand how plugins work',
    'dependencies':[] # Write down your script's dependencies here
}

def info():
    """
    Returns information about the plugin.
    """
    return PLUGIN_METADATA

def register_args(parser):
    """
    Register arguments for the demo plugin.
    """
    parser.add_argument('--me', type=str, help='Function for the demo plugin')

def execute(args):
    """
    Run the code in here
    """
    if args.me:
        print(f"This plugin is name {__file__}")
