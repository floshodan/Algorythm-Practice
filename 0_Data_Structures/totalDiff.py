
sensorA = [15, -4, 56, 10, -23]
sensorB = [14, -9, 56, 14, -23]


def totalDiff(sensorA, sensorB, size):
	dif = 0
	for i in range(len(sensorA)):
		dif += abs(sensorA[i] - sensorB[i]) 
	return dif

print(totalDiff(sensorA, sensorB, 5))
