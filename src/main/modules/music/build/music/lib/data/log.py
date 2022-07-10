from .dataitem import DataItem

def Event(Enum):
	PLAY      = 1

def Log(DataItem):
	timestamp = ''
	action    = Event.PLAY
	duration  = ''

DataItem.add_child(Log,'logs')