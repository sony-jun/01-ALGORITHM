# 영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 
# 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.
# 성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

N, M = map(int,input().split())
matrix = [list(map(int, input().split() for _ in range(n)))]

#줄에 X 카운트, 1line당 X>1 이상일 경우 카운트 하지않고, 반대의 경우는 카운트한다
count=0
for i in range(n):
    if "X" in matrix[i]:
        cnt +=1

print(cnt)
