import re, os
import data, main, spotify
from runner import RunnerDaemon
from dataitem import MappableItem
from play import play

def is_cmd(msg):
    return re.match('^music.*',msg)

def run_cmd(cmd):
    local_table = data.get_tables()
    songs = local_table['songs'].copy()
    cmd = re.sub("music\.py","music",cmd)
    if cmd == 'music':
        if len(songs.columns) > 0:
            songs = songs.drop(axis=1,columns='id')
            print(songs)
    elif "play" in cmd:
        print("playtime")
        play(cmd,local_table)
    elif "rate" in cmd:
        item = MappableItem(cmd,'user').item
        if '-d' in cmd:
            spotify.unpause_player()
        item.save()
    else:
        if len(cmd) > 0:
            print('-'+cmd+'-\nThe above command was not parsable')

def run_message(message):
    if is_cmd(message):
        run_cmd(message)