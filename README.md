# photorename_addshotdate
> Python 3.8.3

## Workflow
1. Read all files in the folder and only process photos (according to file suffix).
2. For each photo, inquire file information to get the shot date.
   - if EXIF information is available, take 'EXIF DateTimeOriginal' as the shot date;
   - otherwise, take the last modification date as the shot date.
3. Rename the photo file in 2 alternative modes:
   - \[Default\] Add shot date as a prefix {yymmdd_} to the filename;
   - Rename the photo file in format {yymmdd}.
   - If multiple photos were shot on the same date, add suffix {\_2, \_3, ...}.
4. After renaming all the photos, the folder will be popped up.

## Usage
- Basic: put the `.py` file in the photo folder and execute the following command.
```
$ python photorename_addshotdate
```
- Option `-r | --mode_rename`  
  The default mode is prefix mode. Use this option to enable rename mode.
```
$ python photorename_addshotdate -r
$ python photorename_addshotdate --mode_rename
```
- Option `-p | --path`  
  The default working folder is where the `.py` file exists. Use this option to change to another folder.
```
$ python photorename_addshotdate -p [path to designed folder]
$ python photorename_addshotdate --path [path to designed folder]
```
- Option `-h | --help`  
  Use this option for instructions about all the options.
```
$ python photorename_addshotdate -h
$ python photorename_addshotdate --help
```
