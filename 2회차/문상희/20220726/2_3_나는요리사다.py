# 문제부터 제대로 읽자!!!

lst = []
for i in range(5):
    lst.append(sum(list(map(int, input().split()))))

print(lst.index(max(lst)) + 1, max(lst))