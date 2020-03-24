import os
from file import File, get_path

def write(file_name, message, overwrite=False):
    mode = 'w' if overwrite else 'a'
    file = File(file_name, mode)
    file.write(message)

def read(file_name, overwrite=False, splitlines=False):
    file = File(file_name)
    text = file.read(overwrite)
    if(splitlines):
        return text.split('\n')
    return text

def does_exist(file_name):
    path = get_path(file_name)
    return os.path.exists(path)