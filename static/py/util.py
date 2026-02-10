import re
from  pathlib import Path
from shutil import copy2
import flags



def slug(s)->str:
"""Define function slug to produce standard url names"""
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





