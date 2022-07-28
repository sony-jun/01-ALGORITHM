import sys

sys.stdin = open("5_덩치_input.txt")

N = int(input())

size = []
for i in range(N):
    a = list(map(int, input().split()))
    size.append(a)
#print(size) #[[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
# 1등은 5점, 2등은 4점, 3등은 3점, 4등은 2점, 5등은 1점
#차등 점수 주고 이걸 각각 몸무게랑 키를 한다음
# 딕셔너리에 부여
size_d = {}

for both in range(len(size)):
    size_d[both] = 0
print(size_d)    
    #for i in range(size):
        


