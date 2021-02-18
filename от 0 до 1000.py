a = [1]
y = 2
cnt = 1
sum_number1 = 0
sum_number2 = 0
summary1 = 0
summary2 = 0
while y<=1000:
	if (y % 2) != 0:
		a.append(y**3)
	y = y + 1
print(a)
for index in range(len(a)):
	a_cut1 = a[index]
	a_cut2 = a[index] + 17
	while cnt<=9:
		sum_number1 = a_cut1 % 10 + sum_number1
		a_cut1 = a_cut1 // 10
		sum_number2 = a_cut2 % 10 + sum_number2
		a_cut2 = a_cut2 // 10
		cnt = cnt + 1
	if (sum_number1 % 7) == 0:
		summary1 = a[index] + summary1
	if (sum_number2 % 7) == 0:
		summary2 = a[index] + 17 + summary2
	sum_number1 = 0
	sum_number2 = 0
	cnt = 1
print("первая сумма", summary1, ', вторая сумма', summary2)