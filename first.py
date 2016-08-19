#Exercise 1.3 - first.py

import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

liveFirstBirths = 0
liveOtherBirths = 0
lengthOf1stPregnancy=0;
lengthOfOtherPregnancy=0;


for pregnancy in table.records:
	#print pregnancy.outcome
	if pregnancy.outcome==1 :
		if pregnancy.birthord == 1 : 
			liveFirstBirths = liveFirstBirths+1
			lengthOf1stPregnancy=lengthOf1stPregnancy+pregnancy.prglength
		else : 
			liveOtherBirths = liveOtherBirths+1
			lengthOfOtherPregnancy=lengthOfOtherPregnancy+pregnancy.prglength

print 'Number of Live Births: ', liveFirstBirths + liveOtherBirths
print 'Number of Live First Births: ', liveFirstBirths
print 'Number of Live Other Births: ', liveOtherBirths
print 'Average 1st Pregnancy', lengthOf1stPregnancy/liveFirstBirths
print 'Average Other Pregnancy', lengthOfOtherPregnancy/liveOtherBirths

#Average pregnancy length



