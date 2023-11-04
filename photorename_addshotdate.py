# python=3.8.3
# coding=utf-8

'''
@File   photorename_addshotdate.py
@Time   2022/08/18
@Author TaylorGy 
@Site   https://github.com/taylorgy
@Desc   Read exif information of photos and get the 'EXIF DateTimeOriginal',
        then add shot date as a prefix {yymmdd_} to the filename.
        If exif is not available, add the last modification date.
'''

import os
import sys
import argparse as argp
import exifread
import datetime

# dir_root = os.getcwd()
# mode_rename = False
IMGSUFFIX = ['.jpg', '.jpeg', '.png', '.tiff', '.webp', '.heic']
FIELD = 'EXIF DateTimeOriginal'

parser = argp.ArgumentParser(description='set photo folder path and rename mode.')
parser.add_argument('-p', '--path', default=os.getcwd(),
    help="path to photo folder, default=current folder")
parser.add_argument('-r', '--mode_rename', action='store_true',
    help="add shot date as prefix or rename file, default=add prefix")
args = parser.parse_args()


def main(args):
    dir_root = args.path
    mode_rename = args.mode_rename

    if not os.path.exists(dir_root):
        print("Please input a valid path!")
        return False
    else:
        # print(dir_root)
        os.chdir(dir_root)
        print("\nWelcome to photo renamer!")
        print("folder: {}\n mode_rename: {}\n".format(dir_root, mode_rename))

    for file in os.listdir('.'):
        filestr = os.path.splitext(file)
        filename   = filestr[0].replace(' ', '_')
        filesuffix = filestr[1].lower()
        if filesuffix in IMGSUFFIX:
            print("reading {}".format(file))
            with open(file, 'rb') as f:
                tags = exifread.process_file(f, details=False)
            # print(tags)
            
            if not tags or FIELD not in tags.keys():
                print('No {} found, use last modification date'.format(FIELD))
                timestamp_m = os.path.getmtime(file)
                shotdate = str(datetime.date.fromtimestamp(timestamp_m))[2:].replace(':', '')
            else:
                shotdate = tags[FIELD].values[2:10].replace(':', '')

            if not mode_rename:
                newfilename = "{}_{}{}".format(shotdate, filename, filesuffix)
                tot = 1
                while os.path.exists(newfilename):
                    tot += 1
                    newfilename = "{}_{}_{}{}".format(shotdate, filename, tot, filesuffix)
            else:
                newfilename = "{}{}".format(shotdate, filesuffix)
                tot = 1
                while os.path.exists(newfilename):
                    tot += 1
                    newfilename = "{}_{}{}".format(shotdate, tot, filesuffix)
            
            os.rename(file, newfilename)
            print("renamed to {}\n".format(newfilename))
    os.startfile('.')


if __name__ == "__main__":
    main(args)