# row = []
# [row.append(i) for i in range(46) for j in range(i)] # 메모리에 올려놓음       
# A, B = map(int, input().split()) # 입력
# print(sum(row[A-1:B])) # 출력


# row = []
# for i in range(0, 46):
#     for j in range(i):
#         row.append(i)

#

N_list = []
A, B = map(int, input().split())
N = 1

# 수열이 B보다 커질때까지
while len(N_list) < B:
    # N의 길이동안
    for _ in range(N):
        # N_list에 추가
        N_list.append(N)
    # N에 1 누적    
    N += 1

print(sum(N_list[A-1:B])) 
    