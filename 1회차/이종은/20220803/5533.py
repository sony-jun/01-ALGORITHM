# 1~100이하의 정수를 카드에 적어 제출 
# 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수의 점수를 얻음
# 첫쨰줄 참가자의 수 n

n = int(input())

score = [[], [], []]
sum = []


for i in range(n): # 인원수 만큼 반복
    a, b, c = map(int, input().split())
    score[0].append(a) # 첫번쨰 숫자, 두번째 숫자, 세번째 숫자들을 따로따로 리스트로 만들어 입력을 받아줌
    score[1].append(b)
    score[2].append(c)
    # 해당 작업을 통해 아래 두번째 행렬로 바뀜

'''
89 92 77
89 92 63
89 63 77
'''    

'''
score
    0  1  2
0 : 89 89 89
1 : 92 92 63 
2 : 77 63 77
'''
# 가로, 세로를 바꿈
# 가로 줄 별로 겹치는 것이 있는지, 
# 겹치는 것이 없다면 인덱스 행렬과 카운트를 통해 1개임, 그 숫자를 sum 리스트에 추가
# 겹치는 것이 있다면, 다시 위에 돌아가다가, 3번 반복 완료 되면 0 출력, 왜냐면 숫자 중복이 있을 때는 변수에 저장 되는 것이 0이 어야 됨
# 겹치는 것이 두개 있을 떄도 다시 위로 돌아감 
# 위로 돌아가다가 겹치는게 계속 있어서 0으로 카운트 되어서 최종 0이되고 다음 인원으로 반복문 시작 
# 두번쨰 인원 경우, 겹치는게 2번 있어서 0으로 카운트 되다가 세번째 겹치는 것이 없어서 63이 출력 됨 
# 세번째 인원 경우, 겹치는게 두번째에 한번 있어서, 두번째 축척 된 점수인 63이 sum에 추가 됨


for i in range(n): # 인원수 만큼 반복
    s_score = 0 # 카운트하기 위해 변수 초기화

    for j in range(3): # 게임 횟수만큼 반복 
        if score[j].count(score[j][i]) == 1: #score가 0,0인 값 즉, 89인 것이 0번째줄에 몇 개있는가? 89 경우 3개 있어서 
            # 1) 0, 0 => 89 => 3개 => # sum 리스트에 0이 추가 됨
            # 2) 1, 0 => 92 => 2개 => # sum 리스트에 0이 추가 됨
            # 3) 2, 0 => 77 => 2개 => # sum 리스트에 0이 추가 됨
            # --- 두번째 인원 수 
            # 1) 0, 1 => 89 => 3개 => # sum 리스트에 0이 추가 됨
            # 2) 1, 1 => 92 => 2개 => # sum 리스트에 0이 추가 됨
            # 3) 2, 1 => 63 => 1개 => # sum 리스트에 63이 추가 됨
            # --- 3번쨰 인원 수 
            # 1) 0, 2 => 89 => 3 개 => # sum 리스트에 0이 추가 됨
            # 2) 1, 2 => 63 => 1개 # sum 리스트에 63이 추가 됨
            # 3) 2, 2 => 77 => 2개 => # sum 리스트에 기존 있었던 63이 추가 됨

            s_score += score[j][i] #
    sum.append(s_score) 
for i in sum:
    print(i)


