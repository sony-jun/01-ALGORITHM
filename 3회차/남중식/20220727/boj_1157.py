T = input()

T = T.lower()
T_dict = dict()

for c in T:
    if T_dict.get(c):
        T_dict[c] += 1
    else:
        T_dict[c] = 1

dict_values = list(T_dict.values())
max_dict_values = max(dict_values)

if dict_values.count(max_dict_values) > 1:
    print("?")
else:
    for k, v in T_dict.items():
        if v == max_dict_values:
            print(k.upper())