# 나는 요리사다

order = 0 # 순서 저장
result = 0  # 최종 점수 저장

for i in range(5): # 5번 입력값을 반복하며 받는다.
    score = list(map(int, input().split())) # 나열하여 입력하는 입력값을 리스트에 담아준다.
                                            # result에 값을 저장하기 위해

    if sum(score) > result: # 현재 합계 점수가 이전의 합계 점수보다 크다면
        result = sum(score) # result에 새로운 값을 저장한다. 
        order = i + 1     # 입력한 순서를 나타내기 위해 i에 1을 더하여 현재 입력 순서를 나타낸다. 
        				  # i는 0부터 시작하므로 현재 순서 값을 저장하기 위해서는 +1 한다. 

print(order, result)





