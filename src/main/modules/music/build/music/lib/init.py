def init_env():
	bashrc.add_line('shopt -s extdebug')

	dynamic_rating_cmd = '''val=$BASH_COMMAND && REGEX=
	&& if [[ $val =~ $REGEX ]]; then python $HOME/Documents/Coding/Active/spools/music/src/music.py 
	`cat $HOME/.spools/music/info.txt` $val && false; else true; fi'''
	bashrc.add_trap('DEBUG',dynamic_rating_cmd)

	bashrc.add_cmd_regex_filter('music',"^[0-9]{1,2}\.[0-9]$")