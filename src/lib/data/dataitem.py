class FileItem(object):
    {
        'attrs': {
            'artist': 'artist',
            'album' : 'project',
            'track' ; 'track'
        }
    }

class DataItem(object):
    def save_table(name):
        data.save_table(name)

    def save(self):
        data.save_item(self)

    def equals(self, other):
        if other == None:
            return False
        return self.id == other.id

class ItemTable():
    def __init__(self, name, itemtype):
        self.module = sys.modules[__name__]
        self.name = name
        self.dataitemtype = itemtype
        self.file = #
    
    def add(item):
        table = pd.read_json(self.file)
        table = table.append(item.to_dict())
        table.to_json(self.file)

class MappableItem(DataItem):
    def __init__(self, param=None, map_type=None):
        self.table = ItemTable(blah)
    
    def to_dict():