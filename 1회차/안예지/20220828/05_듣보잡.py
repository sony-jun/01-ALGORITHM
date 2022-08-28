# 1764
"""
1. 듣보잡인 사람은 명단에 두 번 등장하므로 딕셔너리로 등장 횟수를 저장
2. 두 번 이상 등장한 사람의 이름을 사전 순으로 출력한다.
"""
import sys
sys.stdin = open("듣보잡.txt")

N, M = map(int, input().split())

double = {}
for _ in range(N + M):
    key = input()
    double[key] = double.get(key, 0) + 1

answer = []
for key in double:
    if double[key] >= 2:
        answer.append(key)
        
answer = sorted(answer)
print(len(answer))
print(*answer, sep = '\n')