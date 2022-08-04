#리스트로 접근

chessboard = [1, 1, 2, 2, 2, 8]  #원래 체스판에 있어야 할 체스의 개수

chess = list(map(int, input().split())) #input되는 체스의 개수

for i in range(len(chess)):  #리스트의 개수만큼 반복
    print(chessboard[i]-chess[i], end = ' ')   #각 리스트의 같은 인덱스의 값을 빼주면 필요한 값이 공백으로 나옴
