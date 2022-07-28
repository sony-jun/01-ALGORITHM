N = int(input())
# 전체 사람의 키와 몸무게를 2차원 리스트로 입력받음
list_hw = [list(map(int, input().split())) for _ in range(N)]

# 등수가 들어가는 리스트 초기화
rank_hw = [1 for i in range(N)]

# 순위를 매겨야 함
# 원소 별로 비교를 해서
# 키와 몸무게가 본인보다 큰 사람이 있을 때마다 카운팅을 +1 한다.
# 예시 
# list_hw[0][0] < list_hw[1][0] and list_hw[0][1] < list_hw[1][1] => +1
# 00 10 01 11
# 00 20 01 21
# 00 30 01 31
# 00 40 01 41

# 10 00 11 01
# 10 20 11 21
# 10 30 11 31
# 10 40 11 41

for i in range(N):
    for j in range(N):
        # 본인과 비교를 하면 안되므로 i와 j가 다를 때, 조건문이 있어서 없어도 무관.
        if i != j:
            # 키와 몸무게 둘 다 본인보다 크다면 등수가 하나씩 증가
            if list_hw[i][0] < list_hw[j][0] and list_hw[i][1] < list_hw[j][1]:
                rank_hw[i] += 1
            else:
                continue
        else:
            continue

for i in range(len(rank_hw)): # 불필요
    print(rank_hw[i], end=' ')



'''
# 사람의 수 N 입력
N = int(input())

list_ = []
# 각 사람의 몸무게와 키 입력
for i in range(N):
    weight, height list(map(int, input().split()))
    # 리스트에 몸무게와 키를 저장
    list_.append((weight,height))

ranks = [0] * N

# 모든 사람을 비교하기 위한 이중반복문
for a in range(N):
    # 기준이 되는 사람
    A = list_[a]

    for b in range(N):
        # 비교가 되는 사람
        B = list_[b]

        # A가 B보다 덩치가 큰지 조건문이 필요합니다.
        # B가 A보다 덩치가 작다
        if A[0] > B[0] and A[1] > B[1]:
            # B보다 덩치가 큰 사람이 한명 더 있다 +1
            ranks[b] += 1
            
for rank in ranks:
    print(rank + 1, end = ' ')
'''