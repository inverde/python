import re
import flags
# Define function slug to use to produce standard url names
def slug(s)->str:
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





