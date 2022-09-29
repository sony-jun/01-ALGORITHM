# https://www.acmicpc.net/problem/23253
# 문제23253번.자료구조는 정말 최고야
# 시간제한:1초, 메모리제한:1024MB



# 입력
'''
1. 교과서 수 N, 교과서 더미의 수 M
- 1 <= M <= N <= 200,000
- 2M줄에 걸쳐 각 더미의 정보가 주어짐
2. i번째 더미에 쌓인 교과서의 수 ki
- 1 <= ki
3. ki개의 교과서의 번호
- 아래에 있는 교과서의 번호부터 주어짐
- 1 <= 교과서의 번호 <= N
'''



# 출력
'''
1. 올바른 순서대로 교과서를 꺼낼 수 있다면 Yes, 불가능하다면 No를 출력
- 1번부터 N번의 교과서 순으로 꺼내야 함
'''



# 코드 1
import sys

sys.stdin = open('input_text/23253.txt')

N, M = map(int, input().split())

# M개의 각 더미에 쌓인 교과서들 기록
stacks = []   
for _ in range(M):
    books_N = int(input())   # 한 더미 내 교과서 갯수
    stacks.append(list(map(int, input().split())))

# 1번부터 N번까지 순서대로 교과서 꺼내기
rst = 'Yes'
for n in range(1, N + 1):   # n: 찾고자하는 교과서
    # 각 더미의 젤 위에 있는 교과서가 찾고자하는 교과서인지 확인
    for books in stacks:   # books: 각 더미 내 교과서들
        if books and books[-1] == n:
            books.pop()
            break
    # break없이 종결됐다면, 각 더미의 젤 위에 원하는 교과서가 없음을 의미
    else:
        rst = 'No'
        break

print(rst)



# 실행결과(실패:시간초과)



# 코드 2
import sys

sys.stdin = open('input_text/23253.txt')

N, M = map(int, input().split())   

# 각 더미 내 교과서들이 크기순대로 쌓였는지 확인
rst = 'Yes'
for _ in range(M):
    books_N = int(sys.stdin.readline())
    books = list(map(int, sys.stdin.readline().split()))
    for i in range(0, books_N - 1):      
        # 크기순대로 쌓이지 않은 경우
        if books[i] < books[i + 1]:
            rst = 'No'
            break
    if rst == 'No':
        break

print(rst)



# 실행결과(메모리:52340KB, 시간:376ms)