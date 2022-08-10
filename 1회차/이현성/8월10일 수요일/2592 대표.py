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

value_ = [value for key, value in dic.items()]
s = max(value_)
dic2 = {value:key for key, value in dic.items()}

print(int(sum(lis) / 10))
print(dic2.get(s))