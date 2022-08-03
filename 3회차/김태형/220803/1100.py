# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.
b=0
board = [input() for i in range(8)]
for i in range(4):
    for j in range(4):
        if board[2*i][2*i]=='F':
            b+=1
        if board[2*i+1][2*i+1]=='F':
            b+=1
print(b)

# A = [1,2,3,4,5,6]
# for i in range(len(A)//2):
#     print(A[2*i],A[2*i+1])