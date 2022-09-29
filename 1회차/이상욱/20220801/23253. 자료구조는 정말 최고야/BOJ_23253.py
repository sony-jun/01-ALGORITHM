lst_1 = [3, 1]
lst_2 = [4, 2]
result = []

while len(result) != 4:
    result.append(lst_1.pop())
    result.append(lst_2.pop())

    print(result)
    print(result.sort())