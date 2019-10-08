"""
Usage:
	music play
    music play <song>
    music play -a <album>
    music play -r <artist>
    music play -s <song>
    music play new

Options:
	-a 		Album name
	-s   	Song name
	-p  	Pause
	-d 		Use id instead of name
	-q 		Quiet
"""

def play_new_album():
	monitor.set_mode('album')
	if is_queue_empty():
		print('Your queue is empty. Please add some albums or artists to your queue')
	else:
		queue.add_new_albums(5)
		spotify.play_queue()
    
def play_new_singles():
	monitor.set_mode('song')

def play_alias():

def play_tag():

def play_genre():

def play_song():

def play_artist():



def play():