from collections import Counter

counter = Counter()

lst = ['ben','bibin','ben','nikhil','vishal']

for name in lst:
    counter[name]+=1
'''
print(counter)
#Counter({'ben': 2, 'bibin': 1, 'nikhil': 1, 'vishal': 1})

print(counter['ben'])
del counter['vishal']

print(f"Counter after deletion: {counter}")

print("\nElements!")
print(list(counter.elements()))

print("\nMost common!")
print(counter.most_common())
'''
print(f"Actual counter: {counter}")
print(counter.values()) # dict_values created | p.s for just values list(counter.values())
print(list(counter)) #Lists unique elements
print(dict(counter)) #converts to normal dictionary
print(set(counter)) #converts to a set

print("\n")
print(counter.items()) #creates dict_items eg: dict_items([('ben', 2), ('bibin', 1), ('nikhil', 1), ('vishal', 1)])
