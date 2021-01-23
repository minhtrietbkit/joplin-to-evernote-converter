# Command to run the tool from terminal: python3 main.py --joplin-dir <absolute-path-to-joplin-export-dir> --evernote-dir <absolute-path-to-joplin-output-dir>, now I run the test to verify that the evernote files are written correctly.

import sys
import os
import shutil
import argparse
from evernote_generator.evernote_generator import EvernoteGenerator

def count_number_joplin_notebook( absolute_path_to_joplin_dir ):
    return len(os.listdir(absolute_path_to_joplin_dir))

def main(*args):
    parser = argparse.ArgumentParser()

    parser.add_argument("joplin_dir", help="absolte path to joplin export directory")
    parser.add_argument("evernote_dir", help="absolte path to evernote output directory")

    args = parser.parse_args(args)

    print(args.joplin_dir)
    print(args.evernote_dir)

    evernote_generator = EvernoteGenerator(args.evernote_dir)
    joplin_parser = JoplinParser(args.joplin_dir)

    # for j_nb_name in os.listdir(args.joplin_dir):
        # evernote_generator.add_notebook(j_nb_name)
    #    for note in nb:
        #    evernote_nb.add_note(note)
    for j_nb in joplin_parser.get_notebooks():
        e_nb = evernote_generator.add_notebook(j_nb.name)
        for j_n in j_nb:
           e_nb.add_note(j_n)

if __name__ == '__main__': 
    main(sys.argv[1:])
    