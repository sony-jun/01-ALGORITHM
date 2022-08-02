from re import A

import sys
input = sys.stdin.readline

names = dict()
n = int(input())

for _ in range(n):
    name = input()
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

for _ in range(n-1):
    name = input()
    names[name] -= 1

for key in names:
    if names[key] > 0:
        print(key)


'''INPUT값을 살펴보면, 3명의 참석자를 알려주고, 그 뒤에 완주자를 알려줘.
뒤에서 입력받지 못한 값이 : 탈락자. 인거지.
후에 입력받은 이름이 같은 값에 -1을 해주면 1인 사람이 탈락자. 
동명이인이 있을 수 있다<<라는 게 dictionary로만 저장하면 안되고 ,
defaultdict 로 해야한다는 거구나..'''

##다른사람이 푼거 읽어보고 해석해보고 썼는데 시간초과 뜬다 얘야...
