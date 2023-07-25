import argparse
from .get_path import *

def argParser():
    parser = argparse.ArgumentParser(description='Describe Arguments for File Organizer')
    parser.add_argument('-p', '--path', type=str, help='Your name')
    args = parser.parse_args()
    if args.path == None:
        args.path = get_folder_path()
    print(args.path)
    return args

# argParser()