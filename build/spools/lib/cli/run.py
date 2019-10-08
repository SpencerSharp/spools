import sys
def run():
    # command = docopt(__doc__, version='Alpha v0.1', options_first=True)
    command = sys.argv[1]
    try:
        command = command_map[command]
    except:
        command = command
    to_run = '{}()'.format(command)
    exec(to_run)