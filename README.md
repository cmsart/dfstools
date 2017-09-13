# DFSTools
A small collection of Python scripts to help with NFL DFS research and analysis. These are just quick scripts I put together for personal use, so the code is not very clean or optimized. These scripts are only for NFL and will not work with other sports.

## Vegas Odds
Pulls data from the [ESPN Daily Lines](http://www.espn.com/nfl/lines) and creates a CSV with the projected team total and average team total from previous games for each team. The current week's total is not included in the average.

Run `python vegas.py` and enter the week you want to gather odds for.

For future NFL seasons, you will need to modify the "season" parameter in the url variable on line 16 to match the current year.

## Exposure
Takes in a DraftKings contest CSV and a list of usernames and outputs the exposure to every player used by each user.

Run `python exposure.py`, enter the path to the DK contest CSV file, and then enter one or more space separated DK usernames (not case sensitive).  
