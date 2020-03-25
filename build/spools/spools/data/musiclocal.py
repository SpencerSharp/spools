def get_path(table_name):
    return abs_path + '/' + table_name

def acquire_key():
    global key
    key = open(abs_path + '.key', 'w')

def release_key():
    key.close()

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
    for table_name in DataItem.table_names():
        load_table(table_name)

def local_exists():
    return os.path.exists(abs_path)