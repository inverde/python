#!/usr/local/bin python
"""
util.py

Usage examples
 # Comment out instrumentation in all .py files (dry run)
 python 

import re
from  pathlib import Path
from shutil import copy2
import flags

# Markers used in source files
START_MARKER = r"// INSTRUMENTATION START"
END_MARKER = r"// INSTRUMENTATION END"

#


def slug(s)->str:
    """
    Define function slug to produce standard url names
    """
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s.strip())
    s = re.sub(r'-+', '-', s)
    return s


def main()->None:
    print(slug('Balance scale with data and fairness'))


if __name__=='__main__':
    if flags.is_debug_mode():
        main()





