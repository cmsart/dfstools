from bs4 import BeautifulSoup
import urllib2

week = input('Enter week: ')
teams = {
			'ARI': [], 'ATL': [], 'BAL': [], 'BUF': [], 'CAR': [], 'CHI': [], 'CIN': [], 'CLE': [], 'DAL': [], 'DEN': [], 'DET': [], 'GB': [], 
		 	'HOU': [], 'IND': [], 'JAX': [], 'KC': [], 'LAR': [], 'MIA': [], 'MIN': [], 'NE': [], 'NO': [], 'NYG': [], 'NYJ': [], 'OAK': [], 
		 	'PHI': [], 'PIT': [], 'LAC': [], 'SEA': [], 'SF': [], 'TB': [], 'TEN': [], 'WSH': []
		}

print 'Scraping data...'

#scrape data for each week
for i in range(1, week + 1, 1):

	url = 'http://m.espn.com/nfl/dailyline?week=' + str(i) + '&season=2017&seasonType=2&wjb'
	response = urllib2.urlopen(url)
	html = response.read()

	soup = BeautifulSoup(html, 'html.parser')
	table = soup.find("table")

	rows = []
	for p, tr in enumerate(table.contents):
		rows.append([])
		for td in tr.contents:
			for string in td.strings:
				rows[p].append(string)
	
	del rows[0] #remove table header

	for row in rows:
		team1 = row[0].strip()
		team2 = row[1].strip()
		team1spread = row[4].strip()
		team2spread = row[6].strip()
		ou = float(row[8].strip())

		if team1spread == 'EVEN':
			spreadsign = 'EVEN'
			spreadnum = 0
		else:
			spreadsign = team1spread[0]
			spreadnum = float(team1spread[1:])

		if spreadsign == '-':
			favorite = team1
			underdog = team2
		else:
			favorite = team2
			underdog = team1
		
		spreadsplit = spreadnum / 2
		ousplit = ou / 2

		favoritetotal = ousplit + spreadsplit
		underdogtotal = ousplit - spreadsplit

		teams[favorite].append(favoritetotal)
		teams[underdog].append(underdogtotal)

print 'Writing results to file...'

#write to file
name = 'week' + str(week) + 'totals.csv'
f = open(name, 'w')
f.write('Team,Current Week,Season Average\n')
for key in sorted(teams.keys()):
	arr = teams[key]
	#get total for current week and remove from list
	currentweek = str(arr[-1])
	del arr[-1]
	if week != 1:
		teamsum = sum(arr)
		teamavg = teamsum / len(arr)
	else:
		teamavg = 0
	f.write(key + ',' + currentweek + ',' + "{0:.2f}".format(teamavg) + '\n')
f.close()

print name + ' has been created!'