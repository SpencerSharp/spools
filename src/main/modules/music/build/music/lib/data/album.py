import numpy as np
from .dataitem import DataItem

class Album(DataItem):
	id          = ''
	name        = ''
	user_rating = np.nan
	log_ids     = []

	field_maps = {
	'internal': {
		'id': 'id',
		'name': 'name',
		'user_rating': 'user_rating',
		'log_ids': 'log_ids',
		},
	'disk': 	{
		'id': 'id',
		'name': 'name',
		'user_rating': 'user_rating',
		'log_ids': 'log_ids',
		},
	'spotify' : {
		'id'  : "['id']",
		'name': "['name']"
		},
	}

	def __init__(self, map_type, map_obj):
		for key,val in Album.field_maps[map_type].items():
			if(type(val) == str):
				val = 'map_obj{}'.format(val)
				to_exec = 'self.{0} = {1}'.format(key,val)
				#print(to_exec)
				exec(to_exec)

	def flag(self):
		return '-a'

DataItem.add_child(Album,'albums')