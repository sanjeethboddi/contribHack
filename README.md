# contribHack

## How to use it?

* Download/Clone the repo to your computer.

* Run the python script
```
python hack.py [-h] -f  [-d] [-p] [-r]

optional arguments:
  -h, --help       show this help message and exit
  -f , --folder    path to the folder/repo
  -d , --days      no. of days in future committed.
  -p , --pattern   path to pattern file
  -r, --refresh    deletes previous commits
```
### Examples

* `python hack.py -f ~/repo_name -d 200 -p ./patterns/hireme -r`
```
This will create a repository called repo_name if a repo/folder with that name doesn't exist in the home folder.
Fills it with empty commits till the date which is 200 days ahead of you. 
This uses hireme pattern to fill. 
-r flag is used to delete all the previous commits made in past.
```
* `python hack.py -f ~/repo_name -r`
```
This will create a repository called repo_name if a repo/folder with that name doesn't exist in the home folder.
Fills it with empty commits till the current date.
Since no pattern file is provided it will fill randomly.
-r flag is used to delete all the previous commits made in past.
```

## Make a custom pattern
* Your pattern file is like a grid with dimensions of 7\*X. (7 rows and X>0 columns)
* Each cell in the grid represents number of commits to be made on a day.
* Look at patterns/hireme for reference.

## Future Additions:
* A GUI tool which helps in creating customized patterns.
