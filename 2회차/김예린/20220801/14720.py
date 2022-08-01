# 우유 축제
'''
딸기우유 = 0
초코우유 = 1
바나나우유 = 2
'''

n = int(input())
milk_street = map(int, input().split())

milk = [0, 1, 2]
cnt = 0

for i in milk:
    for j in i:
        if i == j:
            cnt += 1