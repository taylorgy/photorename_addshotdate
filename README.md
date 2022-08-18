# photorename_addshotdate
> add or rename photo based on the shot date  
> based on Python 3.8

## system workflow
1. read all files in the folder and only process photos (according to file suffix).
2. for each photo, inquire about file information to get the shot date.
   - if EXIF information is available, take 'EXIF DateTimeOriginal' as the shot date;
   - otherwise, take the last modification date as the shot date.
3. rename the photo file in 2 alternative modes:
   - \[default] add shot date as a prefix of the filename in format "yy-mm-dd_";
   - rename the photo file in format "yy-mm-dd".
   - if multiple photos were shot on the same date, add suffix "\_2, \_3, ..." to the duplicate files.
4. after renaming all the photos, the folder will be popped up.

## usage
- basic: put the `.py` file in the photo folder and execute the following command.
```
$ python photorename_addshotdate
```
- option `-r | --mode_rename`  
  the default mode is prefix mode. use this option to enable rename mode.
```
$ python photorename_addshotdate -r
$ python photorename_addshotdate --mode_rename
```
- option `-p | --path`  
  the default working folder is where the `.py` file exists. use this option to change.
```
$ python photorename_addshotdate -p [path to designed folder]
$ python photorename_addshotdate --path [path to designed folder]
```
- option `-h | --help`  
  use this option for instructions about all the options.
```
$ python photorename_addshotdate -h
$ python photorename_addshotdate --help
```
  
