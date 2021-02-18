duration = int(input('enter a number of seconds'))
time = [1, 60, 3600, 86400, 2592000, 31104000]
count = [0, 0, 0, 0, 0,0]
y = 5
while y >= 0:
	c = duration // time[y]
	duration = duration - c * time[y]
	count[y] = c
	y=y - 1
print ( count[5], 'years', count[4], 'months', count[3], 'days', count[2], 'hours', count[1], 'minutes', count[0], "seconds")