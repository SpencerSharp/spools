from daemon.monitor import create_monitor
import env.bashrc.bashrc as bashrc
from restapis.spotify import get_spotify_permissions
from filesys.data.data import load_data
import os
def init_env():
    if not os.path.exists('/Users/spencersharp/.spools/test/music'):
        os.mkdir('/Users/spencersharp/.spools/test/music')
    os.system('touch /Users/spencersharp/.spools/test/music/monitor_block')
    bashrc.add_line('shopt -s extdebug')
    get_spotify_permissions()

    bashrc.add_cmd_regex_filter('music',"^[0-9]{1,2}\.[0-9]$")

def init():
    init_env()
    create_monitor()
    load_data()