class Track(object):
    field_maps = {
        'disk': {
            'id': '.id',
            'name': '.name',
            'user_rating': '.user_rating',
            'tags': '.tags'
        },
    
    def current():