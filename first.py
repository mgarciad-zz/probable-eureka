#Exercise 1.3 - first.py

import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

liveBirths = 0

for pregnancy in table.records:
	#print pregnancy.outcome
	if pregnancy.outcome==1 : liveBirths=liveBirths+1

print 'Number of Live Births: ', liveBirths