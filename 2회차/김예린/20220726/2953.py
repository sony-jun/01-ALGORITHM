# 나는 요리사다
highest = 0 # 최댓값이 있는 순서
result = 0  # 최종 점수를 저장할 변수

for i in range(5): # 입력을 5번하기 때문에
    score = list(map(int, input().split())) # 나열하여 입력하는 입력값을 리스트에 담아준다.
                                            # result에 값을 저장하기 위해

    if sum(score) > result: # 더해진 값이 전의 합계 점수보다 크다면
        result = sum(score) # result에 새로운 값을 저장한다. 
        highest = i + 1     # 입력한 순서를 나타내기 위해 i에 1을 더하여 현재 입력 순서를 나타낸다. 
                            # 총 5번의 순서 중 i는 현재 순서를 나타내기 때문에

print(highest, result)






