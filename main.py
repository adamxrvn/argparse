import argparse
import datetime
import os

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--size", help="Print size in MB of the file", action="store_true")
parser.add_argument("-m", "--mtime", help="Print modification time. Arguement: 12/24 (for time format)", nargs='?',
                    const=24, type=int)
parser.add_argument("-r", "--rename", help="Change file name to B", nargs='?',
                    const=os.path.basename(__file__), type=str)

args = parser.parse_args()

st = os.stat(__file__)

if args.mtime:

    if args.mtime == 12:
        timestamp = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%d-%m-%Y %l:%M')
    else:
        timestamp = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%d-%m-%Y %H:%M')
    print(f'last modified: {timestamp}')

if args.size:
    print(f'file size: {st.st_size / (1024 ** 2)} MB')
if args.rename:
    os.rename(os.path.basename(__file__), args.rename)
