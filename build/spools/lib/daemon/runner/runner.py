# import sys, time, curses, os, signal, psutil
# from .args import ArgsFile
# from .monitor import monitor

# music_home  = os.environ['HOME'] + '/.spools/music/'
# runner_file = 'runner'
# cmds_file   = 'cmds'

# def runner(perms, data):
# 	signal.signal(signal.SIGUSR1, parseargs)
# 	signal.signal(signal.SIGUSR2, unpause)

# 	runnerpid = get_runner_pid()

# 	while os.getpid() == runnerpid:
# 		signal.pause()


# def get_runner_pid():
# 	path = music_home + runner_file
# 	if not os.path.exists(path):
# 		return -1
# 	file = open(path, 'r')
# 	result = file.read()
# 	file.close()
# 	return int(result)

# def is_runner():
# 	pid = os.getpid()
# 	runner = get_runner_pid()

# 	return pid == runner

# def does_runner_exist():
# 	pid = get_runner_pid()
# 	try:
# 		os.kill(pid, 0)
# 		runner_create_time = psutil.Process(pid)._create_time
# 	except:
# 		return False
# 	return True

# def set_runner_pid(pid):
# 	path = music_home + runner_file
# 	file = open(path, 'w')
# 	file.write(str(pid))
# 	file.close()

# def is_runner_child():






# def create_runner(perms, data):
# 	if os.fork() > 0:
# 		sys.exit()
# 	elif os.fork() > 0:
# 		sys.exit()
# 	set_runner_pid(os.getpid())
# 	runner(perms, data)

# export SPOTIPY_CLIENT_ID='b4847d3dd2464848bc7f1f34b04f9509'
# export SPOTIPY_CLIENT_SECRET='1ebd017edc044803906b36e81bd48cc3'
# export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
# shopt -s extdebug
# export SPOOLS_MUSIC_HOME='$HOME/.spools/music'
# export SPOOLS_MUSIC_PATH='/Users/spencersharp/Documents/Coding/Active/spools-music/src/music.py'
# export SPOOLS_MUSIC_ARGS='cat /Users/spencersharp/.spools/music/info.txt'
# trap 'val=$BASH_COMMAND && REGEX="^[0-9]{1,2}\.[0-9]$" && if [[ $val =~ $REGEX ]]; then python $SPOOLS_MUSIC_PATH `$SPOOLS_MUSIC_ARGS` $val && false; else true; fi' debug

# trap 'val=$BASH_COMMAND && REGEX="^[0-9]{1,2}\.[0-9]$" && if [[ $val =~ $REGEX ]]; then python $SPOOLS_MUSIC_PATH `$SPOOLS_MUSIC_ARGS` $val && false; else true; fi' DEBUG