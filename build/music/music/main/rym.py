
profile_url = 'https://rateyourmusic.com/~{}'
export_url = 'https://rateyourmusic.com/user_albums_export?album_list_id={}&noreview'

class RYM(API):
    def get_user_id_from_username(username):



class RYMUser(object):
    def __init__(self, username):
        self.username = username
        self.id = RYM.get_user_id_from_username(self.username)
    
    def import_ratings():

