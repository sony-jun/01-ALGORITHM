# 7785
"""
1. 로그의 최종 상태를 이름 별로 갱신해야 하므로 딕셔너리 사용
2. 공백으로 구분하여 '이름:상태' 쌍의 딕셔너리 생성
3. 사전의 역순으로 출력해야 하므로 sorted함수를 사용하여 역순으로 출력
 
"""
import sys
sys.stdin = open("회사.txt")

n = int(input())
logs = {}

for _ in range(n):
    words = input().split()
    logs[words[0]] = words[1]

answer = []
for name in logs:
    if logs[name] == 'enter':
        answer.append(name)

# answer = sorted(answer, reverse = True)
# print(*answer, sep = '\n')