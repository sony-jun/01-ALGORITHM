numbers = []
for i in range(3):
    number = str(input())
    numbers.append(number)
for i in numbers:
    maximum = 1
    cnt = 1
    for j in range(len(i) - 1):
        if  i[j] == i[j + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > maximum:
            maximum = cnt
    print(maximum)