# 첫 째 줄에 교과서의 수 N, 교과서 더미의 수 M
# 둘째줄부터 2 * M에 걸쳐 더미의 정보
# 4 2 -> 4권, 2더미
# 2   -> 첫번째 더미, 2권
# 3 1 -> 3 위에 1이 있음
# 2   -> 두번째 더미, 2권
# 4 2 -> 4위에 2가 있음
import sys

input = sys.stdin.readline # 빠른입력 
N, M = map(int, input().split()) # 교과서의 수, 더미의 수 입력받음

for i in range(M):
    b_dummy = int(input()) # 더미의 정보(한 더미에 책이 몇개인지)
    book = list(map(int, input().split())) # 교과서의 번호

    for j in range(b_dummy-1): # 한 더미 내의 책의 수 -1
        if book[j] < book[j+1]: # 더미 내 책과 그 다음책의 번호를 비교
            print("No") # 다음 책 번호가 더 크면 NO
            exit(0) # 정상종료 
print("Yes")