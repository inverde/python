#!/usr/local/bin python
"""
util.py

Usage examples
 # Comment out instrumentation in all .py files (dry run)
 python util.py --path src --ext py --action comment --dry-run

 # Actually modify files and keep backups
 python util.py --path src --ext py --action comment --backup

 # Uncomment instrumentation
 python util.py --path src --ext py --action uncomment --backup

 """
import re
import argparse
from  pathlib import Path
from shutil import copy2
import flags

# Markers used in source files
START_MARKER = r"// INSTRUMENTATION START"
END_MARKER = r"// INSTRUMENTATION END"

# For Python files we willl use '#' to commnet; for other languages you can adapt
COMMENT_PREFIX = "# "

def process_text(text:str, action:str, comment_prefix:str) -> str:
    """
    Replace blocks between START_MARKER and END_MARKER.
    - action == "comment": replace block contents with commented lines
    - action == "uncomment": remove leading comment_prefix from lines inside block
    """
    pattern = re.compile(
        rf"({re.escape(START_MARKER)}\n)(.*?)(\n{re.escape(END_MARKER)})", re.DOTALL
    )

    def replacer(m):
        start, body, end = m.group(1), m.group(2), m.group(3)
        lines = body.splitlines()
        if action == "comment":
            # If already commented, leave as-is
            commented = []
            for ln in lines:
                if ln.strip() == "":
                    commented.append(ln)
                elif ln.strip().startswith(comment_prefix.strip()):
                    commented.append(ln)
                else:
                    commented.append(comment_prefix + ln)
            new_body = "\n".join(commented)
        elif action == "uncomment":
            uncommented = []
            for ln in lines:
                # Remove only one leading comment_prefix if present
                if ln.lstrip().startswith(comment_prefix.strip()):
                    # Preserve original indentation
                    leading_ws = ln[: len(ln) - len(ln.lstrip())]
                    uncommented.append(leading_ws + ln.lstrip()[len(comment_prefix.strip()):])
                else:
                    uncommented.append(ln)
            new_body = "\n".join(uncommented)
        else:
            raise ValueError("action must be 'comment' or 'uncomment'")
        return start + new_body + end
    new_text, n = pattern.subn(replacer, text)
    return new_text
def process_file(path: Path, action:str, dry_run: bool, backup:bool, comment_prefix:str)->None:
    """
    Function that reads a file, processes its text, and writes changes back to disk with optional backup
    and dry-run behaviour
    """
    # Reads the file contents as UTF-8
    original = path.read_text(enconding="utf-8")

    # Transforms the file contents using the process_text function
    modified = process_text(original, action, comment_prefix)

    # If no changes were made, skip writing and report that the file was skipped
    if original == modified:
        print(f"[SKIP] {path}")
        return
    print(f"[MODIFY] {path}")
    # If dry_run is true , report the planned modification but do not writhe changes to disk
    if dry_run:
        print("  (dry-run) changes not written")
        return
    if backup:
        bak = path.with_suffix(path.suffix + ".bak")
        copy2(path,bak)
        print(f"  backup -> {bak}")
    path.write_text(modified, enconding="utf-8")
    print("  written")

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
    parser =

if __name__=='__main__':
    if flags.is_debug_mode():
        print(slug('Balance scale with data and fairness'))
        #Example usage: process a single file for demonstration
        p = Path("example.py")
        process_file(p, action="comment", dry_run=True, backup=Flae, comment_prefix=COMMENT_PREFIX)

