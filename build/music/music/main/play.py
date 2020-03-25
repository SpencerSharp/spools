import spotify
"""
Usage:
	music play
    music play <song>
    music play -a <album>
    music play -r <artist>
    music play -s <song>
    music play new a|s [-t]

Options:
    -r      Artist name
	-a 		Album name
	-s   	Song name
	-p  	Pause
	-d 		Use id instead of name
	-q 		Quiet
"""

def play(cmd, table):
    spotify.make_playlist("rabbittown")

# def play_new_album():
# 	monitor.set_mode('album')
#     if queue.size() < 10:
#         albums = get_from_backlog('album', 10)
#         queue.add(albums)
# 		queue.play()
#     else:
#         print('Please add more albums to your backlog')

# def play_new_singles():
# 	monitor.set_mode('song')
#     if queue.size() < 100:
#         songs = get_from_backlog('song', 100)
#         queue.add(songs)
#         queue.play()
#     else:
#         print('Please add more songs to your backlog')

# def play_alias():

# def play_tag():

# def play_genre():

# def play_song():

# def play_artist():

