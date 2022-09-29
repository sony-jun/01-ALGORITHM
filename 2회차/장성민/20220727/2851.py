# 답을 위한 변수 선언
result = 0

# 10번을 돌며 점수 입력 받고, 점수 누적
for i in range(10):
    score = int(input())
    result += score

    if result >= 100:
        
        # 현재 result에서 방금 입력받은 score 차감한 값을 one에,
        # result에서 100 차감한 값을 two에 담는다
        one, two = 100 - (result - score), abs(result - 100)
        
        # result - score 값이 100에 더 가까울 때
        if one < two:
            result -= score
            break
        
        # result가 100에 더 가까울 때
        elif two < one or one == two:
            break

print(result)
