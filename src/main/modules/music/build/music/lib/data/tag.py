from .dataitem import DataItem

# Make "Favorite" a builtin tag
def Tag(DataItem):
	id = 0
	name = ''
	subgenre_ids = []

	# Redundant but helpful - If we make a runner, don't save this data, just construct it on init
	parent_ids   = []
	album_ids    = []
	song_ids     = []

DataItem.add_child(Tag,'tags')