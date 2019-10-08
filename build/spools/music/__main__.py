#!/usr/bin/env python3
"""
Usage:
    music
    music <command> [<args>...]

Commands:
    music p|play
    music r|rate
    music q|queue
    music s|skip
    music i|import
    music m|me
    music b|backlog
    music c|categorize
    music a|alias
    music l|login
    music t|trim
    music -h|--help
    music -o|--options
    music -v|--version
    music -q|--quit
"""
from lib import *
from rate import rate
from cli import main
from restapis.spotify import get_spotify_permissions
from lib.data.album import Album
from lib.data.song import Song
from cli import init
init.init()
get_spotify_permissions()
rate()

command_map = {
   'import' :'imprt'
}

# print(cli.main)