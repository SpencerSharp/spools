"""
Usage:
    music rate [-cdpq] (-a|-s) <name>...

Options:
	-a 		Album name
	-s   	Song name
	-c      Current song/album
	-d 		Use spotify id instead of name
	-p  	Pause
	-q 		Quiet
"""
import os, sys,signal
import pandas as pd
from docopt import docopt

from lib.data 		import save_data
from lib.spotify 	import get, search
from data.dataitem  import DataItem



def rate():
	args = docopt(__doc__)

	if 		args['-a']:
		type   = 'album'
	elif 	args['-s']:
		type   = 'song'

	if      args['-d']:
		id     = args['<name>'][0]
	else:
		id    = search('album', ' '.join(args['<name>'][:-1]))

	if 		args['-c']:
		item = spotify.current()
	else:
		item = get(type, id)

	item.user_rating = round(float(args['<name>'][-1:][0]),1)

	save_data(item)

	if(type=='album' and args['-d'] and not args['-q']):
		fantano()

def fantano():
	print('\nDid you love it, did you hate it, what would you rate it?')
	