import csv, string

delimiters = ['QB', 'RB', 'WR', 'TE', 'FLEX', 'DST']

def main ():
	file_name = raw_input('Filename: ')
	with open(file_name, 'rb') as f:
		reader = csv.reader(f)
		contest = list(reader)

	users = raw_input('Enter players: ')

	for user in users.split():
		user = user.strip()
		players = {}
		num_lineups = 0
		username = ''

		for row in contest:
			name = row[2].split()[0].strip()

			# if the name matches the one we are looking for, parse the lineup
			if name.lower() == user.lower():
				username = name
				lineup = row[5]
				player = ''
				num_lineups += 1
				for word in lineup.split():
					if word in delimiters:
						if player != '':
							# check for player and add/increment
							player = player.strip()
							if player in players:
								players[player] += 1
							else:
								players[player] = 1
							# reset player string
							player = ''
					else:
						player += word.strip() + ' '

		# put exposures into list for csv creation
		exposures = []
		for i, player in enumerate(players):
			exposures.append([])
			exposures[i].append(player)
			uses = players[player]
			percent = (float(uses) / float(num_lineups)) * 100
			exposures[i].append(str(round(percent, 2)) + '%')

		# add headers for csv
		header = ['Player', 'Exposure']
		exposures.insert(0, header)

		# create csv
		if num_lineups == 0:
			print user + ' does not have any lineups in this contest.\n'
		else:
			filename = username + '-exposure.csv'
			with open(filename, "wb") as f:
			    writer = csv.writer(f)
			    writer.writerows(exposures)

			print username + ' created ' + str(num_lineups) + ' lineups.'
			print filename + " created!\n"

main()