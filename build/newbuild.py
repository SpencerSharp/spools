'''
from spools import env




'''

from pathlib import Path

base = Path('/Users/spencersharp/Documents/Coding/Active/spools')
build_path = base / 'build'

def reset():
    src_path = base / 'src'
    build_path.unlink()
    shutil.copytree(src_path, build_path)



def collapse(dir):
    if 'src' in dir.iterdir():
        collapse_module(dir)
    else if dir.name == 'src':
        collapse_src(dir)
    else if dir.name == 'modules':
        collapse_modules(dir)


reset()
collapse(build_path)