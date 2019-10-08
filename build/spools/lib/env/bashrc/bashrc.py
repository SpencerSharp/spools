# bashrc = open(os.environ['HOME'] + '/.bashrc', 'r')
# 	already_saved = False
# 	for line in bashrc:
# 		if 'DEBUG' in line:
# 			already_saved = True
# 	bashrc.close()
# 	bashrc = open(os.environ['HOME'] + '/.bashrc', 'a')
# 	if not already_saved:
# 		bashrc.write(dynamic_rating_cmd)
# 	bashrc.close()
# 	os.system('. ~/.bashrc')

def add_line(ln):
	n = ln

def add_trap(signal, cmd):
	n = 0

def add_cmd_regex_filter(cmd,regex):
	dynamic_rating_cmd = '''val=$BASH_COMMAND && REGEX=
	&& if [[ $val =~ $REGEX ]]; then python $HOME/Documents/Coding/Active/spools/music/src/music.py 
	`cat $HOME/.spools/music/info.txt` $val && false; else true; fi'''
	add_trap('DEBUG',dynamic_rating_cmd)