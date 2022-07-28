
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 1 = 2초 2('ABC') = 3초 

import sys

sys.stdin = open("15_다이얼.txt")

dial = ['ABC' , 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
push = input()
time = 0
for i in push:
    for j in dial:
        if i in j:
            time += dial.index(j) + 3 # 1번째 자리 dial[0]이 3초기 때문에 +3을 한다.
print(time)