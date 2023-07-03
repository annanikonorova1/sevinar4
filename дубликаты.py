nabor_1=input('Введите элементы списка:')
nabor_1=list(nabor_1)
temp = []
for x in list(nabor_1):
    if x not in temp:
        temp.append(x)
nabor_2 = {x for x in nabor_1 if nabor_1.count(x) > 1}
nabor_1 = temp
print(nabor_2)
print(f'список после удаления дубликатов = {temp}')