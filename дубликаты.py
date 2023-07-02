nabor_1=input('Введите элементы списка:')
nabor_1=list(nabor_1)
temp = []
for x in list(nabor_1):
    if x not in temp:
        temp.append(x)

nabor_1 = temp

print(f'список после удаления дубликатов = {temp}')