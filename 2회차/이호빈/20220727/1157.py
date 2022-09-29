alphabet = list(map(str, input().upper()))

dictionary = {}
result = []
values = 0

for i in alphabet:
    dictionary[i] = dictionary.get(i, 0) + 1

values = list(dictionary.values())
values_1 = list(dictionary.keys())

if values.count(max(values)) > 1:
    print("?")
else:
    max_alpha = values.index(max(values))
    print(values_1[max_alpha])
    
    
