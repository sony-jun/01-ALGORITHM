import sys
sys.stdin = open('대표값.txt', 'r')

lis = []
for _ in range(10):
    lis.append(int(input()))

dic = {}
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_value = max(dic.values())

max_key = []
for key, value in dic.items():
    if value == max_value:
        max_key.append(key)

max_key = sorted(max_key)

# print(int(sum(lis) / 10))
# print(max_key[0])
print(dic.values())