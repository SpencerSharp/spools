
base = Path('/Users/spencersharp/Documents/Coding/Active/spools')

def reset():
    src_path = base / 'src'
    build_path = base / 'build'

    build_path.unlink(missing_ok=True)

    old_lib_path = src_path / 'lib'
    new_spools_path = build_path / 'spools'
    new_spools_path.mkdir()

    shutil.copytree(old_lib_path, new_spools_path)
    modules = src_path / 'main' / 'modules'
    for module in modules.iterdir():
        new_module_path = build_path / module.name
        new_module_path.mkdir()
        shutil.copytree(module, new_module_path)
reset()