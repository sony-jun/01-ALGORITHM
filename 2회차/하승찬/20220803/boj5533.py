# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	2538	1827	1708	74.132%
# 문제
# 상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다.

# 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.

# # 상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.
# import sys


# sys.stdin = open("input.txt", "r")
#  플레이어의 점수를 라운드별로 정리하여 비교값을 만든다.
#  각 플레이어의 점수를 for문으로 순환하게만든 후 각 열의 점수를 비교값리스트에 넣어서 같은 수가 1개일때 더해준 후 더한 값을 출력한다.


# 1. 행과 열을 받아 리스트를 만든다. 
# 2. 열을 기준으로 게임 라운드마다 나온 점수들의 리스트 (rs) 에 넣어준다 
# 3.  각 행의 점수들을 만들어둔 rs의 리스트에 넣어서 카운트로 카운팅 된 숫자가 1일때 출력한다.

n = int(input())

games = [list(map(int,input().split())) for __ in range(n)]#입력받기


rs= []

# for j in range(3):  각 플레이어의 점수를 ins의 리스트에 넣은 후 비교값리스트 rs에 넣어준다 리스트로 묶여서 넣어야기에 ins 리스트를 임시로 만들어서 사용
ins =[]
for i in range(n): 
    ins.append(games[i][j])
rs.append(ins) 



# for k in games: 플레이어의 점수를 for문으로 순환시켜서 각 라운드마다 점수를 하나씩 비교값에 넣어 count로 카운팅한다.
sum =0
for j in range(3):
    if rs[j].count(k[j])==1: #카운트가 1일 때 sum 변수에 입력값을 더해준 후 
        sum+=k[j]
print(sum)                 # for문이 종료되면 sum 값을 출력되게 만든다.



# for s in games:
#     for k in range(len(s)):
         


