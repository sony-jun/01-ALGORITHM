# 백준 유니크 5533
# 상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다.
# 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.
# 상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.
N = 3
M = int(input())
matrix_1 = [[],[],[]]
for i in range(M):
    matrix_1.append(list(map(int, input().split())))
for idx in range(N):
    ready = []
    for index in range(M):
        ready.append(matrix_1[index][idx])
    for i_i in range(1, M):
        print(ready)


