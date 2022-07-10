import shutil
from pathlib import Path

base = Path('/Users/spencersharp/Documents/Coding/Active/spools')

def flatten(to_flatten):
    for item in to_flatten.iterdir():
        # print(item)
        if item.is_dir():
            if to_flatten.name == 'modules':
                build_module(item)
            else:
                flatten(item)
                for sub in item.iterdir():
                    shutil.move(sub, to_flatten / sub.name)
                shutil.rmtree(item)

def build_module(module):
    src_path = module / 'src'
    build_src(src_path)
    build_library(module / module.name)
    module_build_path = module / 'build'
    if module_build_path.exists():
        shutil.rmtree(module_build_path)
    make_module_setup(module)

def make_module_setup(module):
    setup_file = module / 'setup.py'
    if not setup_file.exists():
        setup_file.touch()
        setup_file.write_text('''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{}", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )'''.format(module.name))

def build_src(module_src):
    if not module_src.exists():
        return
    build_library(module_src / 'lib')
    build_main(module_src / 'main')
    shutil.move(module_src, module_src.parent / module_src.parent.name)

def build_main(module_main):
    modules_dir = module_main / 'modules'
    if modules_dir.exists():
        for module in modules_dir.iterdir():
            if module.name == '.DS_Store':
                continue
            build_module(module)

def build_library(module_lib):
    if not module_lib.exists():
        return
    if module_lib.parent.name != 'lib':
        main_file = module_lib / (module_lib.parent.name + '.py')
    else:
        main_file = module_lib / (module_lib.name + '.py')
    if main_file.exists():
        init_file = module_lib / '__init__.py'
        if not init_file.exists():
            init = '''import pkg_resources
pkg_resources.declare_namespace(__name__)
{}'''.format(main_file.read_text())
            init_file.touch()
            init_file.write_text(init)
    recurse = []
    for fil in module_lib.iterdir():
        if fil.is_dir():
            recurse.append(fil)
    for fil in recurse:
        build_library(fil)

# wtf does this function do
def reset():
    build_path = base / 'build'
    if build_path.exists():
        shutil.rmtree(build_path)
    build_path.mkdir()
    (build_path / 'spools').mkdir()

    shutil.copytree(base / 'src', base / 'build' / 'spools' / 'src')
    build_module(base / 'build' / 'spools')

    shutil.move((build_path / 'spools' / 'spools').as_posix(), base / 'tmp')
    shutil.rmtree(build_path)
    shutil.move(base / 'tmp', build_path)
    (build_path / 'main' / 'modules' / 'spools').mkdir()
    shutil.move(build_path / 'lib', build_path / 'main' / 'modules' / 'spools' / 'spools')
    shutil.move(build_path / 'main' / 'modules', base / 'tmp')
    shutil.rmtree(build_path)
    shutil.move(base / 'tmp', build_path)

    make_module_setup(build_path / 'spools')
    shutil.copy(base / 'README.md', build_path / 'spools' / 'README.md')

reset()
