import sys
sys.stdin = open("20220802/1269_대칭차집합.txt")
input = sys.stdin.readline

N = int(input())        # N개의 수

num = []
for i in range(N):      # N번
    n = int(input())    # 정수 입력받아
    num.append(n)       # 리스트에 추가

num.sort()              # N개의 수 리스트 정렬

for i in range(N):
    print(num[i])       # 순서대로 출력