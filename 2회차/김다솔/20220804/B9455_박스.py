import sys
sys.stdin = open('B9455.txt')

T = int(input())
for tc in range(T):
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]
    # print(box)
    
    #이중반복문, 열부터 순회 
    for x in range(n): # 행순회, 아래에서 위로
    # for y in m-1, -1, -1 거꾸로 하는 방법
    #reversed(range(행개수))
        for y in list(range(m))[::-1]:
            if box[y][x] == 박스? :
                while true:
                    if 
                    box[y+1][x] != box and y+1 != m :
                    box[y][x] = empty
                    box[y+1][x] = box
                    y += 1