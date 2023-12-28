PLUGIN_METADATA = {
    'name': 'Demo Plugin',
    'version': '1.0',
    'author': 'Camille.Is_Me',
    'description': 'A demo plugin for the plugin system, and for the users so that they have a template to go off of.',
    'dependencies' : ['datetime'] #Fill out with your plugin's dependencies
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
    parser.add_argument('--me', type=str, help="Simple function to print the file's name.")
    parser.add_argument('--date', type=str, help="Simple function to print the current date.")

def execute(args):
    """
    Execute the whole plugin.
    """

    import datetime
    #Here we import the libraries we need and
    #have listed above in the plugin's metadata

    #And here is where we execute the code depending on 
    #what arguments were provided.
    if args.me:
        print(__file__)

    if args.date:
        print(datetime.datetime.now())
