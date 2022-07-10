"""
Usage:
    music backlog add
    music backlog remove
    music backlog top
    music backlog [-cdpq] (-a|-s) <name>...

Options:
    -a      Album name
    -s      Song name
    -d      Use spotify id instead of name
    -p      Pause
    -q      Quiet
"""

def backlog():
    
def add_to_backlog(item):
    item.user_rating = np.nan
    item.save()

def get_from_backlog(type, count):
    