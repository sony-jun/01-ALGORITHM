# 델타 탐색에선 델타 배열부터 만들어야함
# dy, dx

# 우 우하 하
dy = [0,1,1]
dx = [1,1,0]

BUILDING = "#"
CAR = "X"
VOID = "."

# 숫자가 공백으로 나뉘어져있는 입력
R, C = list(map(int,input().split()))

list = []


# R 줄 만큼의 리스트를 입력 
for _ in range(R):
    # 숫자 X 문자 O
    # 공백 X
    temp_list = list(input())
    list.append(temp_list)
# 이중 반복문
for r in range(R):
    for c in range(C):
        # 차를 부순 횟수는 탐색을 할 떄마다 초기화
        break_count = 0
        # 조건1. 기준 좌표가 빌딩(#)이면 안된다
        if list[r][c] == BUILDING:
            # 이 다음 반복문의 코드들을 무시하고 , 다음 값을 탐색
            continue
            # 성립이 안되는 조건들은 contibue로 지나가고
            # 조건이 성립될 때만 정상적인 코드를 실행한다


            # 조건 2. 기준 좌표가 차라면 부순 횟수 +1 
        if list[r][c] == CAR:
            break_count += 1


        """
        델타 탐색을 하는 로직
        """
        for d in range(3):
            next_r = r + dr[d]
            next_c = c + dc[d]


            # 조건 1. 범위를 벗어나면 안된다
            if not (-1 < next_r < R and -1 < next_c < C):
                break
            # 조건 2. 탐색 좌표에 빌딩이 있으면 안된다
            if list[next_r][next_c]