import os
import file
import pandas as pd

def set_tables(new_tables):
    global tables
    tables = new_tables
    return tables

try:
    n = tables.keys()
except:
    set_tables({'songs': pd.DataFrame()})

def get_tables():
    return tables

def get_table_name(item):
    if type(item) != type:
        item = type(item)
    return item.__name__.lower() + 's'

def create_table(item):
    table_name = get_table_name(item)
    tables[table_name] = pd.DataFrame()

def save_tables():
    for table_name, table in tables.items():
        tables[table_name].to_json(file.get_path(table_name))

def load_tables():
    to_create = []
    new_tables = {}
    for table_name, table in tables.items():
        json_file = file.get_path(table_name)
        if os.path.exists(json_file):
            new_tables[table_name] = pd.read_json(file.get_path(table_name))
        else:
            to_create.append(table_name)
    for name in to_create:
        new_tables[table_name] = pd.DataFrame()
    return set_tables(new_tables)

def save_item(item):
    table_name = get_table_name(item)
    series = item.get_as('dataframe',len(tables[table_name]))
    tables[table_name] = tables[table_name].append(series)
    save_tables()
