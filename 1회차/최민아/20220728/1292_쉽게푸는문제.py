import sys
sys.stdin = open("20220728/1292_쉽게푸는문제.txt")

A, B = map(int, input().split())

num_count = 0               # 수열 최소 개수 구하기
num = 1                     # 어느 숫자까지 추가해야하는지 구하기
while True:
    num_count += num        # 1개, 2개 ... 더하다가
    if num_count >= B:      # B보다 크거나 같으면 탈출
        break
    num += 1

num_list = []               # 수열 만들기
for i in range(1, num+1):   # 1부터 num까지 수열에 추가
    for j in range(i):      # 해당 수만큼 리스트에 넣기
        num_list.append(i)  # 1이면 1개, 2이면 2개 ...

result = 0                  # A번째부터 B번까지의 더하기
for i in range(A-1, B):
    result += num_list[i]

print(result)