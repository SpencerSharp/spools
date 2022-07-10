"""
Usage:
    music import spotify
    music import rym

Options:
	
"""


def from_spotify(all, playlist):
    for playlist in current_user_playlists():
        for local_song in get_playlist(playlist):
            if local_song.is_new():
                local_song.save()

def from_rym():

def imprt():
	arguments = docopt(__doc__)
	print(arguments)