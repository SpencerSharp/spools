from .dataitem import DataItem

def Artist(DataItem):
	id = ''
	name = ''
	album_ids = []

DataItem.add_child(Artist,'artists')