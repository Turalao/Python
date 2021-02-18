procent = int(input('введите число'))
if procent % 10 == 1 and procent % 100 != 11:
	print (procent, 'процент')
elif 2 <= procent %10 <=4 and  (not(12 <= procent % 100 <= 14)):
	print (procent, 'процента')
else:
	print (procent, 'процентов')