lst = []
n = 5
for _ in range(n):
    number = int(input())
    lst.append(number)

lst.sort()
print(sum(lst) // n)
print(lst[2])

