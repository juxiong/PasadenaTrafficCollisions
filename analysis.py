import csv

with open('Traffic_Collisions.csv') as f:
	lines = csv.reader(f, delimiter=',')
	# Column 12 is NoInjured
	# Column 15 is Cause

	causes = {}
	for line in lines:
		if line[15] not in causes:
			causes[line[15]] = 1
		else:
			causes[line[15]] += 1

	sortedCauses = sorted(causes.items(), key=lambda x: x[1], reverse=True)
	print(sortedCauses)