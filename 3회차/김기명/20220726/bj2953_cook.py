point = [0]*5  #대충 포인트를 리스트로 정의해둠. 요소 5개

for i in range(5):
    point[i] = sum(map(int, input().split()))   # 포인트의 각 요소에 입력되는 값들의 합을 넣어줌. 그걸 5번 반복함

winner = 1                  # 리스트는 0부터지만 세는건 1부터니 1번을 승자로 일단 잡음
point2 = point[0]               # 포인트2(승자의 점수) = 첫번째 점수합을 넣어둠

for i in range(5):
    if i == 4:          # 아래의 식에서 i == 4가 되면 point[5] 를 찾게되서 오류가 나므로 4가 될때 순회를 멈춤
        break
    if point[i + 1] > point2:       # 두번째 선수의 점수가, (n+1)번째 선수의 점수가 기존의 승자점수보다 크다면
        winner = i + 2              # 승자번호와 승자점수 교체
        point2 = point[i + 1]
if winner == 1:                 # i + 1로 순회를 해서 첫번째선수가 이길경우는 아래와같이 정의함 .. 필요없는듯 ?? (잘모르겠는데 놔둠)
    point2 = point[0]  

print(winner, point2)
