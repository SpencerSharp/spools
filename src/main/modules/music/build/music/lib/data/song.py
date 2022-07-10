import numpy as np
from .dataitem import DataItem

class Song(DataItem):
	id          = ''
	name        = ''
	user_rating = np.nan
	log_ids     = []

	# Redundant but helpful - If we make a runner, don't save this data, just construct it on init
	# References
	artist_id   = ''
	album_id    = ''
	secondary_artist_ids = []
	genre_ids = []
	tag_ids = []

	# Aggregate stats
	# adjusted_score  = np.nan
	# predicted_score = np.nan

	field_maps = {
	'internal': {
		'id': '.id',
		'name': '.name',
		'user_rating': '.user_rating'
		},
	'disk': 	{
		'id': '.id',
		'name': '.name',
		'user_rating': '.user_rating',
		'log_ids': '.log_ids'
		},
	'array':	{
		'id': '[0]',
		'name': '[1]',
		'user_rating': '[2]'
		},
	'spotify' : {
		'id': "['id']",
		'name': "['name']",
		'artist_id': "['artists'][0]['id']",
		'album_id' : "['album']['id']"
		},
	'spotify-current' : {
		'id': "['item']['id']",
		'name': "['item']['name']",
		'artist_id': "['item']['artists'][0]['id']",
		'album_id' : "['item']['album']['id']"
		}
	}

	def __init__(self, map_type, map_obj):
		for key,val in Song.field_maps[map_type].items():
			val = 'map_obj{}'.format(val)
			to_exec = 'self.{0} = {1}'.format(key,val)
			exec(to_exec)

	def get_as(self, map_type):
		return np.array([[self.id, self.name, self.user_rating, []]])

	def flag(self):
		return '-s'

DataItem.add_child(Song,'songs')