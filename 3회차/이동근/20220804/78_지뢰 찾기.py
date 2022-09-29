# 주의사항 : https://www.acmicpc.net/board/view/82343
# 더 좋은 코드들
# https://www.acmicpc.net/source/41471407
# https://www.acmicpc.net/source/41843437

def get_grid():
    n = int(input())

    landmine = []
    player = []
    
    for i in range(n * 2):
        if i < n:
            landmine.append(input())
        else:
            player.append(input())

    return landmine, player


# 첫 번째 줄 이후에 만약 지뢰를 밟은 것이 있으면
# 첫 번째 줄에서의 지뢰가 있을 경우를 처리해야 하므로
# 반드시 출력 전 지뢰를 밟았는지 안밟았는지를 알아야 한다.
def check_failure(landmine, player):
    ret = False

    n = len(landmine)
    for i in range(n):
        for j in range(n):
            if landmine[i][j] == '*' and player[i][j] =='x':
                ret = True

    return ret


def find_landmine(landmine, player, flag):
    # 방향 결정
    dx, dy = [-1, 0, 1], [-1, 0, 1]
    n = len(landmine)

    for i in range(n):
        for j in range(n):
            # 매 줄마다 초기화
            count = 0
            
            if player[i][j] == '.':
                if landmine[i][j] == '*' and flag:
                    print('*', end='')
                else:
                    print('.', end='')
            else:
                # 발견했는데 지뢰를 밟았을 경우
                if landmine[i][j] == '*':
                    print('*', end='')
                else:
                    # 한 지점에서 살펴봐야 할 부분은 자기 자신을 제외한 총 8개이다.
                    for k in range(3):
                        for l in range(3):
                            # 인덱스 정상 범주 검사
                            if (0 <= i + dx[k] < n) and (0 <= j + dy[l] < n):
                                if landmine[i + dx[k]][j + dy[l]] == '*':
                                    count += 1
                    print(count, end='')
        print()


if __name__ == '__main__':
    landmine, player = get_grid()

    flag = check_failure(landmine, player)

    find_landmine(landmine, player, flag)