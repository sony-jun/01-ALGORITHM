import sys

input = sys.stdin.readline

n = int(input())
dic = {}
for i in range(2*n - 1):
    name = input()
    if dic.get(name) is None:
        dic[name] = 1
    else:
        del(dic[name])

print(*dic)

# for key, val in dic.items():
#     if val == max(dic.values()):
#         print(key)
    
