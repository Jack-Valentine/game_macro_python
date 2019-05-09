#!d:\revolution_macro\macro_module\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'mss==3.1.2','console_scripts','mss'
__requires__ = 'mss==3.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mss==3.1.2', 'console_scripts', 'mss')()
    )
