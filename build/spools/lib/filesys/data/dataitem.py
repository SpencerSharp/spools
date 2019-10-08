import pandas as pd
import numpy  as np
class DataItem(object):
	child_map = {}

	def add_child(child, table_name):
		DataItem.child_map[table_name] = child

	def save_item(data, item_type, item):
		table_name = type(item).__name__.lower() + 's'
		cols = list(DataItem.get_fields(table_name))
		series = pd.DataFrame(np.array(item.get_as('array')), index=[len(data[table_name])], columns=cols)
		return data[table_name].append(series)

	def create_item(type, map_type, item):
		if item != None:
			return DataItem.child_map[type + 's'](map_type, item)

	def table_names():
		return DataItem.child_map.keys()

	def get_fields(table_name, type='disk'):
		return DataItem.child_map[table_name].field_maps[type].keys()