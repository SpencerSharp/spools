import pkg_resources
pkg_resources.declare_namespace(__name__)
#!/usr/bin/env python3
"""
Usage:
    music
    music <command> [<args>...]
"""
from init import init

init()