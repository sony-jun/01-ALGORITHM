# m행 n열로 이루어진 그리드가 주어진다. 일부 칸에는 박스가 들어 있다. 모든 박스가 더 이상 움직일 수 없을 때 까지 아래로 움직인다면, 박스는 쌓여진 상태가 된다.

# 그림 (a)의 그리드의 크기는 5행 4열이고, 7칸에는 박스가 들어있다. 모든 박스가 계속해서 아래로 움직이면, 그림 (b)와 같이 변하게 된다.



# 박스가 움직인 거리는 바닥에 쌓이기 전 까지 이동한 칸의 개수이다. 예를 들어, 맨 왼쪽 열에서 가장 위에 있는 박스가 움직인 거리는 2이다. 모든 박스가 이동한 거리 (각 박스가 이동한 거리의 합) 을 구하는 프로그램을 작성하시오. 위의 예제에서 박스 7개가 움직인 거리는 8이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 m과 n이 주어진다. (1 ≤ m, n ≤ 100) 다음 m개 줄에는 그리드의 각 행의 정보를 나타내는 n개의 정수가 주어진다. 그리드 첫 행부터 마지막 행까지 순서대로 주어진다. 박스가 들어있는 칸은 1로, 다른 칸은 0으로 주어진다. 각 정수 사이에는 공백이 하나 주어진다.
# case = int(input)

from pprint import pprint


#접근 방법 
# 매트릭스를 세로 기준으로 본 후 1의 위치에 따라 움직여야하는 횟수가 증가한다는 점에서 접근
# 위쪽에 존재하는 1은 밑으로 내려가 쌓여야한다.
# 0이 빈공간임으로 1이 0 위에 있으면 1번 움직이게 된다. 그러므로 빈공간만 카운트를 해준다
# 1 아래 1이 있을 경우에는 상자처럼 쌓이게 되어서 밑에서내려가며 만나는 수가 1일 때는 빈공간이 아님으로 카운트를 하지 않는다
# 매트리스를 순회하며 1일 때 세로축을 기준으로 내려가며 0을 카운트 하는 코드를 만들면 전체 움직이는 횟수를 카운트 할 수 있다.

# for testcase in range(int(input())):   
n,m= map(int,input().split()) 

matrix = [list(map(int,input().split())) for __ in range(n)] 

cnt=0
pprint(matrix)
for y in range(n):                                  
    for x in range(m):
        if matrix[y][x] ==1:                                # 매트릭스를 순환하며 숫자가 1이 나오면  가로(x,y)의 y를 고정시킨후 x축만 for문을 돌린다 
            for i in range(y+1,len(matrix)):
                if matrix[i][x] ==0:                        # for문을 돌며 세로로 내려가게하며 0이 나오면 움직여야하니 카운트에 1씩 더해준다.
                    cnt+=1
print(cnt)

        # for i in range(matrix[y][x],matrix[len(matrix[0])][x]):
        #   if i ==0:
        #     cnt+=1

# print(cnt)


# pprint.pprint(matrix)

# # for y in range(m):
# #     ins=[]
# #     for x in range(n):
# #         ins.append(matrix[x][y])
# #     l_matrix.append(ins)

# # for boxs in l_matrix:
# #     for i in range(len(boxs)):
# #         if boxs[i] == '1':
# #             for 
# pprint.pprint(l_matrix)