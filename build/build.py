import os, re, sys, time, subprocess

spools_path = os.environ['SPOOLS_PATH']



time_val = 0

cd = 0
cd_file = ''
path = ''
home = ''
def sleep():
	if time_val != 0:
		local = time_val
		if local < 0.1:
			local = 0.1
		time.sleep(local)
		print(path)

def set_home(param):
	global home
	home = spools_path + '/' + param

def set_path(param):
	global path
	path = param

def bash(cmd):
	cmd = re.sub('self',self(),cmd)
	debug = 'cd {0}/{1} &>/dev/null && {2} &>/dev/null'.format(home,path,cmd)
	val = os.system(debug)
	return val

def rm(var):
	if type(var) == type([]):
		var = ' '.join(var)
	elif(var == self() and cd == 0):
		cd_up()
		res = rm(self())
		cd_down()
		return res
	return bash('rm -rf '+var)

def ls():
	try:
		val = os.listdir('{}/{}'.format(home,path))
	except:
		return []
	return val

def mv(start,end):
	return bash('mv {} {}'.format(start,end))

def cur():
	return path.split('/')

def recurse(file):
	build_dir(path + '/' + file)

def set_cd_file(param):
	global cd_file
	cd_file = param

def change(num):
	set_cd_file(self())
	global cd
	cd += num
	if num > 0:
		set_path(re.sub('/'+cd_file,'',path))
	else:
		set_cd_file('')
		set_path(path+'/'+cd_file)

def cd_up():
	change(1)

def cd_down():
	change(-1)

def self():
	return cur()[-1] if cd == 0 else cd_file

def init(imports,all):
	file_name = '{0}/{1}/__init__.py'.format(home,path)
	file = open(file_name,'w')
	file.write('{0}\n{1}'.format(imports,all))
	file.close()

def repl_self(param, thing):
	return re.sub('self',thing,param)

def patch_main():
	main_path = '{0}/{1}/'.format(home,path)
	main_name = self()+'.py'
	try:
		file = open(main_path+main_name,'r')
		text = file.read()
		text = re.sub('as main', "\nif __name__ == '__main__':\n    main()", text)
		file.close()
		rm(main_name)
		if 'lib' not in cur():
			main_name = '__main__.py'
		file = open(main_path+main_name,'w')
		file.write(text)
		file.close()
	except:
		n = 1

def passes_test():
	try:
		running_path = '{0}/{1}'.format(home,path)
		if '.py' not in path:
			running_path += '/__init__.py'
		val = subprocess.run(['python',running_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		val = len(val.stderr.decode('utf-8'))
		return val
	except:
		return -1
	

files = []
def push_file():
	global files
	if path not in files:
		files.append(path)

def remove_faulty():
	copy = files
	result = []
	result_weights = []
	for temp_path in copy:
		weight = len(temp_path.split('/'))
		if 'spools/lib' in temp_path:
			weight += 20
		ind = 0
		for compare in result_weights:
			if compare < weight:
				result.insert(ind, temp_path)
				result_weights.insert(ind, weight)
				break
			ind += 1
		if ind == len(result_weights):
			result.append(temp_path)
			result_weights.append(weight)
	for sorted_path in result:
		set_path(sorted_path)
		gen_init()
		# No such file = 512
		# 256 = syntax error
		# 0 = good
		#time.sleep(0.02)
		test_attempt = passes_test()
		if test_attempt != 0:
			if sorted_path != 'spools/lib':
				print(path)
				#rm(self())

def display(words):
	print('\n'.join(words))

#print(spools_path)

bad = ['README.md', '^.git.*', '__pycache__','^.?out$','.*test.*']
def build_dir(cur_path):
	set_path(cur_path)
	for baddie in bad:
		if re.match(baddie,self()):
			rm(self())
			return
	if len(ls()) == 0:
		return
	sleep()
	patch_main()
	for file in ls():
		if file == 'build':
			rm('build')
			bash('rsync -a src/ build')
			cd_up()
			if True:
				mv('self/build', 'temp')
				rm('self')
				mv('temp', 'self')
			cd_down()
			build_dir(cur_path)
		elif file == 'main' or file == 'modules':
			mv('{}/*'.format(file),'.')
			rm(file)
			build_dir(cur_path)
		set_path(cur_path)
		recurse(file)
		set_path(cur_path)

def map_files(cur_path):
	push_file()
	set_path(cur_path)
	for file in ls():
		map_files(path + '/' + file)
		set_path(cur_path)

src_bads = ['__init__.py', '__pycache__']
def clean_dir(cur_dir):
	set_path(cur_dir)
	for evil in src_bads:
		rm(evil)
	for sub_dir in ls():
		clean_dir(cur_dir + '/' + sub_dir)

def clean_src():
	set_home('src')
	clean_dir('')

def gen_init():
	if len(ls()) == 0:
		return
	rm('__init__.py')
	dir_files = []
	imports = []
	for sub_file in ls():
		dont_init = ['__pycache__', '__main__.py']
		if sub_file not in dont_init:
			local = re.sub('\.py$','',sub_file)
			dir_files.append(local)
			if '.py' in sub_file:
				imports.append('import {}'.format(local))
			else:
				imports.append('from {} import *'.format(local))
	all = '__all__ = [{}]'.format(','.join("'{}'".format(file) for file in dir_files))
	imports = ['from . import *']
	init('\n'.join(imports),all)
clean_src()
set_home('build')
set_path('')
bash('rm -rf spools')
bash('mkdir spools')
bash('rsync -a ../src/ spools')
set_path('spools')
build_dir(path)
map_files('spools')
remove_faulty()
# for module_path in modules_to_build: 321 590
# 	module_path = '{spools_path}/{module_path}'.format(spools_path=spools_path, module_path=module_path)
# 	os.system('cd {} && rm -rf build'.format(module_path))
# 	os.system('cd {} && rsync -a src/ build'.format(module_path))

# 	removables = ['README.md', '.git', '.gitignore']

# 	module_name = re.sub('.*/','',module_path)

# 	os.system('cd {path}/build && mv {module_name}.py __main__.py'.format(path=module_path,module_name=module_name))
# 	os.system('cd {path}/build && mv main/* . && rm -rf main'.format(path=module_path))

# 	for file in removables:
# 		os.system('cd {path}/build && rm -rf {file}'.format(path=module_path,file=file))
# 	os.system('cd {path} && mv build {module_name} && mkdir build'.format(path=module_path,module_name=module_name))
# 	os.system('cd {path} && mv {module_name} build/{module_name}'.format(path=module_path,module_name=module_name))

# for module_path in module_paths:
# 	lib_path = '{spools_path}/{module_path}/src/lib'.format(spools_path=spools_path, module_path=module_path)
# 	cmd =  '''cd {} && '''.format(lib_path)
# 	cmd += '''find -E . -type d -not -regex '(.*/\..*)' -not -regex '.*__pycache__.*' -not -regex ".*__init__\.py"'''
# 	cmd += ''' -exec ls {} ";" -exec echo {} ";" -exec echo ";" > ''' + file_name
# 	os.system(cmd)
# 	tree_map = {}
# 	with open('{}/.out'.format(lib_path)) as file:
# 		file_contents = file.read()
		
# 		for directory in file_contents.split('\n\n')[:-1]:
# 			files = directory.split('\n')
# 			rel_parent_path = files[-1][1:]
# 			parent_name = re.sub('.*/','',rel_parent_path)
# 			files = files[:-1]

# 			init_contents = []

# 			for file in files:
# 				if file == 'build.py' or file == '.out':
# 					if rel_parent_path == '':
# 						continue
# 				if file == '__init__.py':
# 					continue
# 				if file == '__main__.py':
# 					continue
# 				if file == '__pycache__':
# 					continue
# 				if file == 'README.md':
# 					continue
# 				init_contents.append(re.sub('\.py$','',file))
# 			print(rel_parent_path)
# 			imports = '\n'.join('import {0}.{1} as {1}'.format(parent_name, item) for item in init_contents)
# 			all_ray = '\n__all__=[{}]'.format(','.join('\'{}\''.format(item) for item in init_contents))

# 			init_file = open('{}/{}/__init__.py'.format(lib_path,rel_parent_path),'w')
# 			init_file.write(imports)
# 			init_file.write(all_ray)
# 			init_file.close()

# 			init_file = open('{}/{}/__init__.py'.format(lib_path,rel_parent_path),'r')

# 			tree_map[rel_parent_path] = init_file.read()
# 	#print(tree_map)


