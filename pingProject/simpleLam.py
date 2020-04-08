from functools import reduce

listo = ['1', '10', '14', '21', '24', '25', '29', '31', '33', '34', '39']
today= ['1', '10', '14', '21', '24', '25', '29', '31', '34', '38', '42', '45', '48', '53', '57']
ob = filter(lambda x: True if x not in listo else False, today)
print(list(ob))

totalAge = reduce(lambda acc, val: acc + 1, today,0)
print(totalAge)