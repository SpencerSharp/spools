import sys
from file import File, get_path
class ArgsFile(File):
	def __init__(self):
		self.file_name = 'args'
		self.path = get_path(self.file_name)

	def does_exist(self):
		try:
			super().create()
		except:
			return True
		return False

	def write_args(self, args):
		text = ' '.join(args)
		super().write(text)

	def update_args(self):
		if self.does_exist():
			text = super().read(line=True,remove=True)
			sys.argv = text.split(' ')