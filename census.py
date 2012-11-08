## Kattie Stahl
## census.py
## Cenus notes from class (6.11)


date = file('', 'r')
for line in data
	line = line.strip()
	if '%' not in line:
		continue

	blacklist = ['Region', 'Division', 'Table', 'UNITED STATES', 'population']

	if 'Region' in line or 'Division' in line or 'Table' in line or 'UNITED STATES' in line or 'population' in line:
		continue
	# states = ['Michigan', 'Florida']
	# for states in state:
	# 	if state in line:
	# 		print line
	# 		print

	# print line.strip()

	print line
	print line[:27].strip()
	print line[27:38].strip()
	print line[86:96].strip()
	print line[144:154].strip()
