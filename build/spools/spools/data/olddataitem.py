import pandas as pd
import numpy as np
import data
import spotify

class DataItem(object):
    def save_table(name):
        data.save_table(name)

    def save(self):
        data.save_item(self)

    def equals(self, other):
        if other == None:
            return False
        return self.id == other.id

class ClassifierItem(DataItem):
    def __init__(self, id, name, child_ids):
        self.id = id
        self.name = name
        self.child_ids = []

class MappableItem(DataItem):
    def __init__(self, param=None, map_type=None):
        name = 'Song'
        start = lambda r: param.find(r)+len(r)+1
        arg = lambda s: param[start(s):(lambda x: start(s)+x if x >= 0 else len(param))(param[start(s):].find("-"))]
        things = 'for key,val in '+name+'''.field_maps[map_type].items():
            if map_type == 'user':
                if key in param:
                    exec('self.item{}'.format(val))
            else:
                if type(val) == str:
                    val = 'param'+val
                else:
                    val = 'np.nan'
                to_exec = 'self.{0} = {1}'.format(key,val)
                exec(to_exec)'''
        exec(things)

    def get_fields(self):
        fields = Song.field_maps['disk'].keys()
        return fields

    def get_values(self):
        fields = self.get_fields()
        results = []
        for field in fields:
            exec('results.append(self.{})'.format(field))
        return results

    def get_as(self, map_type, ind):
        df = pd.DataFrame(data=[self.get_values()], index=[ind], columns=self.get_fields())
        return df

# class RatedItem(MappableItem):
#     user_rating = np.nan
#     flag        = ''
#     tag_ids     = []

#     def is_rated(self):
#         if self.user_rating != np.nan

class ParsableItem(MappableItem):
    commands = {

    }
    options = {

    }



class Song(MappableItem):
    flag = '-s'
    field_maps = {
    'user':     {
        '-s':   ' = Song(spotify.get_track_named(arg(key)), "spotify")',
        '-d':   ' = Song(spotify.get_track(arg(key)),"spotify")',
        '-c':   ' = Song(spotify.get_current_track(),"spotify")',
        '-r':   '.user_rating = float(arg(key))',
        '-t':   '.tags = arg(key).split(" ")'
        },
    'disk': {
        'id': '.id',
        'name': '.name',
        'user_rating': '.user_rating',
        'tags': '.tags'
        },
    'array':    {
        'id': '[0]',
        'name': '[1]',
        'user_rating': '[2]',
        'tags': '[3]'
        },
    'spotify' : {
        'id': "['id']",
        'name': "['name']",
        'artist_id': "['artists'][0]['id']",
        'artist_name': "['artists'][0]['name']",
        'album_id' : "['album']['id']",
        'user_rating': np.nan,
        'tags': np.nan
        }
    }


class Album(MappableItem):
    flag = '-a'

# class Album(MappableItem):
#     flag = '-a'
#     field_maps = {
#     'internal': {
#         'id': 'id',
#         'name': 'name',
#         'user_rating': 'user_rating',
#         'log_ids': 'log_ids',
#         },
#     'disk':     {
#         'id': 'id',
#         'name': 'name',
#         'user_rating': 'user_rating',
#         'log_ids': 'log_ids',
#         },
#     'spotify' : {
#         'id'  : "['id']",
#         'name': "['name']"
#         },
#     }

#     def __init__(self, map_type, map_obj):
#         for key,val in Album.field_maps[map_type].items():
#             if(type(val) == str):
#                 val = 'map_obj{}'.format(val)
#                 to_exec = 'self.{0} = {1}'.format(key,val)
#                 exec(to_exec)

#     def flag(self):
#         return '-a'
