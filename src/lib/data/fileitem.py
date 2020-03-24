class FileItem(object):
    def __init__(self, args):
        locals = [find_options(basedir, args)]
        if len(locals) == 0:
            self.find_source()
        else if len(locals == 1):
            self.source = locals[0]
        else:
            raise
    
    def find_options(dir, args):
        for item in dir.iterdir():
            if args[0] in item.name:
                if dir.is_dir():
                    yield find_options(item, args[1:])
                else if len(args) == 1:
                    yield item
    
    def find_source():
        self.source = source
        self.is_saved = False
        

        'attrs': {
            'artist': 'artist',
            'album' : 'project',
            'track' ; 'track'
        }