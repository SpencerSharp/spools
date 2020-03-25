import os, pwd

user = pwd.getpwuid( os.getuid() )[ 0 ]

basedir = Path('/Users/{}/Pictures/Photos Library.photoslibrary/originals'.format(user))