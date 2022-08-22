import sys
sys.stdin = open("52_카드_11652.txt", "r")

N = int(input())

dic = {}
for tc in range(N):
    
    num = input()
    
    if dic.get(num, 0):
        dic[num] += 1
    else:
        dic[num] = 1

print(dic)
dic = sorted(dic.items(), key = lambda x : -x[1])
print(dic)
dic = sorted(dic, key = lambda x : x[0])
print(dic)
print(dic[0][0])