# 프로그래머스
# signs가 [true,false,true] 이므로, 실제 수들의 값은 각각 4, -7, 12입니다.
# 따라서 세 수의 합인 9를 return

def solution(absolutes, signs):
    # signs가 참이면 해당 absolutes의 수가 양수, 거짓이면 음수
    # 주어진 수를 하나씩 접근
    
    answer = 0 # 양수, 음수가 적용된 실제 합 을 계산할 변수 설정
    for i in range(len(absolutes)): #리스트 길이가 3
        #  true인경우 양수이므로 더하기
        if signs[i]: # 두 개 인지의 길이가 같으므로, signs의 인덱싱 값이 true면
            answer += absolutes[i] #answer 변수에 absolutes동일 인덱싱의 값 + 
        # false 인 경우 음수이므로 빼기
        else:
            answer -= absolutes[i] #answer 변수에 absolutes동일 인덱싱의 값 -
    return answer #answer 값 반환

 
