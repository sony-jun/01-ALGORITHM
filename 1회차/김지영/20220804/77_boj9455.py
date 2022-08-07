import sys
sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(n)]
    
    box = 1
    emp = 0
    move = 0

    for y in range(n):  # 열순회 먼저
        for x in reversed(range(m)):  # 행순회, 아래서 부터
            # print(y,x)
            if grid[y][x] == box:
                while  True:
                    if y+1 != m: # 박스는 범위를 벗어나지 않음
                        break
                    if grid[y+1][x] != box: # 박스 아래는 박스가 없음
                        break
                    grid[y][x] = emp
                    grid[y+1][x] = box
                    y+=1
                    move += 1
            print(move)
        
    # print(f'#{test_case} ')