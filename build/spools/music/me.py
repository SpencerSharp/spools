"""
Usage:
	music me top
    music me -a <artist>

Options:
	-a 		Album name
	-s   	Song name
	-p  	Pause
	-d 		Use id instead of name
	-q 		Quiet
"""

from lib.data 		import data

def me():
	print(data['songs'])