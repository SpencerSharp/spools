import os, signal
from restapis.spotify import pause_player, unpause_player, get_artist_name
def prompt_and_get_rating(item):
	info = open('/Users/spencersharp/.spools/test/music/info.txt','w')
	info.write('rate -dpq ' + item.flag() + ' ' + item.id )
	info.close()
	artist_name = get_artist_name(item.artist_id)
	print('\nPlease score and tag "{0}" by {1}: '.format(item.name,artist_name), end='', flush=True)
	pause()

def pause():
	signal.signal(signal.SIGUSR1, wake_on_signal_received)
	pause_player()
	signal.pause()
	unpause_player()
	signal.signal(signal.SIGUSR1, signal.SIG_IGN)

def send_signal(pid, sig):
	if pid > 0:
		os.kill(pid,sig)

def wake_on_signal_received(a,b):
	test = 'fool'