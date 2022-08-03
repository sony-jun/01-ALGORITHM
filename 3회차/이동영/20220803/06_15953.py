import sys

sys.stdin = open("input.txt", "r")

n = int(input())

dp_2017 = [1, 3, 6, 10, 15, 21]
dp_2018 = [1, 3, 7, 15, 31]
dict_2017 = {'1' : 5000000, '3' : 3000000, '6' : 2000000, '10' : 500000, '15' : 300000, '21' : 100000, '0' : 0}
dict_2018 = {'1' : 5120000, '3' : 2560000, '7' : 1280000, '15' : 640000, '31' : 320000, '0' : 0}

for i in range(n):
    
    a, b = map(int, input().split())

    for j in range(len(dp_2017)):
        if a > 21 or a == 0: 
            ranking2017 = 0
        elif a <= dp_2017[j]:
            ranking2017 = dp_2017[j]
            break
 
    for j in range(len(dp_2018)):
        if b > 31 or b == 0: 
            ranking2018 = 0
        elif b <= dp_2018[j]:
            ranking2018 = dp_2018[j]
            break
    
    print(dict_2017[str(ranking2017)] + dict_2018[str(ranking2018)])
    