n, m = map(int, input().split())

castle = []

for _ in range(n): # 가로 n번 반복
    castle.append(input())

row = [] 
col = []

for i in range(n):
    row.append("X" not in castle[i]) # x가 없으면 트루, 있다면 false


for j in range(m): 
    col.append("X" not in [castle[i][j] for i in range(n)]) # i를 고정시켜 놓고 j에 따라서 x가 있는지 판단하여 col에 담기 
    # 세로 줄 탐색 , [castle[i][j]가 세로여서 엑스 없으면 트루, 있으면 false

print(max(sum(row), sum(col))) # x 트루 갯수 구하기

