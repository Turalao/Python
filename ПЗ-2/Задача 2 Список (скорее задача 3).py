start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i=0
while  i<10:
    if not start_list[i].isalnum():
        if len(start_list[i]) > 2:
            start_list[i] = f'"{start_list[i]}"'
        else:
            start_list[i] = f'"+0{start_list[i][1:]}"'
    elif start_list[i].isdigit():
        start_list[i] = f'"{start_list[i]}"'
    i = i + 1
print(' '.join(start_list))
