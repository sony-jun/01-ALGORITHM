
lst = []
s = 0
for _ in range(9):
    n = int(input())
    lst.append(n)
    s += n
for i in range(8):
    for j in range(i+1,9):
        if lst[i] + lst[j] == s - 100:
            del_i = i
            del_j = j
lst.pop(del_i)
lst.pop(del_j-1)

lst.sort()
for result in lst:
    print(result)