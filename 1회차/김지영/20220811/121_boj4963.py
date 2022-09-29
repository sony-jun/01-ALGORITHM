import sys
sys.stdin = open('121_input.txt')

land = 1
sea = 0
# search up,down,left,right
delta = [(1,0),(0,-1),(-1,0),(1,0),(-1,1),(1,1),(1,-1),(-1,-1)]
# pprint
def ppr(lst):
    for i in lst:
        print(i)

# matrix 자체가 0과 1 로 이루어진 True,False list
# search 해서 이어진 영역이 있으면 1 -> 0, 이어진 곳 이동,
# 이어진 곳 없으면, count + 1 하고 다른 1을 찾는다.
while True:
    w,h = map(int,input().split())
    if (w,h) == (0,0) :
        break
    matrix = [list(map(int,input().split())) for _ in range(h)]
    # ppr(matrix)
    cnt = 0
    for y in range(h):
        for x in range(w):
            if matrix[y][x] == land:
                visit_list = [(y,x)]
                matrix[y][x] == False
                cnt += 1

                while visit_list:
                    i,j = visit_list.pop()
                    
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<= ny < h and 0<= nx < w:
                        visit_list[y][x] = False
                        if matrix[ny][nx] == land:
                            cnt += 1
                            # print(f'이동지점 {ny},{nx}')
                            y = ny
                            x = nx
                if cnt > 0:
                    continue
                else : break
                        # else : 
                        #     cnt += 1
                        #     break
            
                        
    # ppr(visited_list)
    print(cnt)