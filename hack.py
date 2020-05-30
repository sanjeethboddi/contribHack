# importing necessary Modules
from datetime import datetime, timedelta, date
import sys
import os
import subprocess
import random
import argparse
from itertools import chain

# Set Arguments parser
parser = argparse.ArgumentParser(description="Hack Github Contribution Graph.")
parser.add_argument("-f", "--folder", metavar='', required=True, help="path to the folder/repo")
parser.add_argument("-d", "--days", metavar='', type=int, default = 0, help="no. of days in future committed.")
parser.add_argument("-p", "--pattern", metavar='', help="path to pattern file")
parser.add_argument("-r", "--refresh", action="store_true", help="deletes previous commits")

args = parser.parse_args()

# Commands
create_dir = "mkdir -p %s"
git_init = 'git init'
git_commit = 'git commit --allow-empty -m "Hackerman"'
commit_date_change = 'GIT_COMMITTER_DATE="%s" git commit --amend --allow-empty --no-edit --date "%s"'
del_all_commits = 'git branch -D master'

# function definitions
def run_command(cmd):
    process = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(error)
        exit()

def get_xth_date(start_date, n):
    tstamp = start_date + timedelta(n+1)
    tstamp = str(tstamp.strftime("%a %d %b %Y 12:12:12 IST"))
    print(tstamp)
    return tstamp

def commit_n_times(n,tstamp):
    for _ in range(n):
        run_command(git_commit)
        run_command(commit_date_change%(tstamp,tstamp))

# Main Funcion
def main():
    # read pattern
    if args.pattern is not None:
        try:
            with open(args.pattern, "r") as pfile:
                pattern = []
                for line in pfile:
                    pattern.append(list(line.strip()))
                pattern = list(map(list, zip(*pattern)))
                pattern = list(chain.from_iterable(pattern))
                pattern_length = len(pattern)
        except:
            print("Error Parsing Pattern \nExitting.....")
            exit()
    else:
        pattern = None

    # Create Repo
    run_command(create_dir%args.folder)
    os.chdir(args.folder)

    # Init GIT
    run_command(git_init)

    # Delete Previous Commits
    if args.refresh:
        run_command(del_all_commits)

    # Filling
    end_date = date.today()
    start_date = end_date - timedelta(371)

    weekday = int(start_date.strftime("%w"))
    start_date = start_date+timedelta(6-weekday)
    end_date = end_date+timedelta(args.days)

    for n in range(int ((end_date - start_date).days)):
        tstamp = get_xth_date(start_date,n)
        if pattern is None:
            commits = random.choice((1,2,3,4,5))
        else:
            commits = int(pattern[n%pattern_length])
        commit_n_times(commits,tstamp)

if __name__=="__main__":
    main()
