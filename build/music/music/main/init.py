import sys, os, time
from clirunner import CLIRunnerDaemon
from monitor import SpotifyMonitorDaemon
from terminal import Terminal
from env import SpoolsBashProfile
import data
from dataitem import Song
import ipc
import spotify

def init_filesys():
    home = os.environ['HOME']
    spools_home_path = '{HOME}/.spools'.format(HOME=home)
    if not os.path.exists(spools_home_path):
        os.mkdir(spools_home_path)
    profile_home_path = '{}/test'.format(spools_home_path)
    if not os.path.exists(profile_home_path):
        os.mkdir(profile_home_path)
    music_home_path = '{}/music'.format(profile_home_path)
    if not os.path.exists(music_home_path):
        os.mkdir(music_home_path)
    daemons_home_path = '{}/.daemons'.format(music_home_path)
    if not os.path.exists(daemons_home_path):
        os.mkdir(daemons_home_path)

def init():
    init_filesys()
    
    runner = CLIRunnerDaemon()

    if runner.exists:
        ipc.send_message_to(runner, " ".join(sys.argv))
        sys.exit()

    bash_profile = SpoolsBashProfile()
    terminal = Terminal(bash_profile)

    monitor = SpotifyMonitorDaemon()

    ipc.send_message_to(monitor,'startup') 
    time.sleep(3)
    ipc.send_message_to(runner, ' '.join(sys.argv))