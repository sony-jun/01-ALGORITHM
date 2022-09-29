import sys
input = sys.stdin.readline
T = 10
result = []
dic = {}
for i in range(T):
    number = int(input().rstrip())
    result.append(number)
    if number not in dic:
        dic[number] = 1
    else:
        dic[number] += 1
new_dic = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
print(sum(result)//len(result))
print(new_dic[0][0])
