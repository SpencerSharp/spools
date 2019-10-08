import os
global music_home
music_home  = os.environ['HOME'] + '/.spools/test/music/'

def get_path(file_name):
	return music_home + file_name

class File(object):
	does_exist = False

	def open(self, mode, close=False):
		self.file = open(self.path, mode)
		if close:
			self.file.close()

	def create(self):
		self.does_exist = True
		self.open('x',close=True)

	def delete(self):
		if os.path.exists(self.path):
			os.remove(self.path)

	def write(self, text):
		self.open('a')
		self.file.write(text)
		self.file.close()

	def read(self, line=True, remove=False):
		self.open('r+')
		text = self.file.read()
		if remove:
			self.delete()
			self.file.close()
			self.open('x')
		self.file.close()
		return text