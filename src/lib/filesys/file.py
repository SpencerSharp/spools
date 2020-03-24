import os
global music_home
music_home  = os.environ['SPOOLS_HOME'] + '/music/'

def get_path(file_name):
	return music_home + file_name

class File(object):
	does_exist = False

	def __init__(self, name, mode='w'):
		self.path = get_path(name)
		self.mode = mode

	def open(self, mode=None, close=False):
		if mode == None:
			mode = self.mode
		self.file = open(self.path, mode)
		if close:
			self.file.close()

	def create(self):
		self.does_exist = True
		self.open('x',close=True)

	def write(self, text):
		self.open()
		self.file.write(text)
		self.file.close()

	def read(self, remove=False):
		self.open('r+')
		text = self.file.read()
		self.file.close()
		if remove:
			self.write("")
		return text