# # 방의 크기 N과 방의 구조가 주어졌을 때, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.

# A = [
#     ['a','.','.','.','.'],
#     ['a','.','.','.','.'],
#     ['a','.','.','.','.'],
#     ['a','.','.','.','.'],
#     ['a','.','.','.','.']
# ]

A = []   
B = []

N = int(input())
for i in range(N):
    n=list(input())    
    A.append(n)

for i in range(N):
    col = [j[i] for j in A]
    B.append(col)

def sleep(m):
    row_sum=0
    row=0
    rows=0
    for j in range(len(m)):
        for i in m[j]:
            if i=='.':
                row_sum+=1
                if row_sum>=2:
                    row=1
            if i!='.':
                row_sum=0
        rows+=row
    return rows

print(sleep(A),sleep(B))
