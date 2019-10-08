from restapis.remote import remote_exists, sync_remote, set_remote, push_to_remote
from filesys.files.file import get_path
from filesys.data.dataitem import DataItem
import os, pandas as pd
rel_path = 'data'
abs_path = get_path(rel_path)
global data
data = {}

def get_path(table_name):
	return abs_path + '/' + table_name

def acquire_key():
	global key
	key = open(abs_path + '.key', 'w')

def release_key():
	key.close()

def save_data(item):
	global data
	data['songs'] = DataItem.save_item(data, 'song', item)
	save_to_local()

def init_table(table_name):
	table = pd.DataFrame(columns=DataItem.get_fields(table_name))
	data[table_name] = table
	table.to_json(get_path(table_name))

def load_table(table_name):
	table = pd.read_json(get_path(table_name))
	data[table_name] = table

def create_local():
	acquire_key()
	if not os.path.exists(abs_path):
		os.mkdir(abs_path)
	for table_name in DataItem.table_names():
		init_table(table_name)

def load_from_local():
	acquire_key()
	for table_name in DataItem.table_names():
		load_table(table_name)

def save_to_local():
	for table_name in DataItem.table_names():
		data[table_name].to_json(get_path(table_name))
	release_key()

def local_exists():
	return os.path.exists(abs_path)

def load_data():
	# This should make sure our .music is either created and pushed to remote or pulled from remote
	if remote_exists():
		sync_remote()
	elif not local_exists():
		create_local()
		set_remote()
		push_to_remote()
	else:
		load_from_local()