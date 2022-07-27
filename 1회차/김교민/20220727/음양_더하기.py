#내가 푼거
def solution(absolutes, signs):
    for i in range(len(absolutes)): #absolutes와 signs의 길이가 같다. 
# absolutes 안의 숫자중 i번째 숫자가 False인경우
# 거짓인 숫자를 음수로 바꾼다음
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
            answer = sum(absolutes) #absolutes의 모든 값을 합한다.
    return answer

#한줄

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

#zip 함수를 이용

def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
