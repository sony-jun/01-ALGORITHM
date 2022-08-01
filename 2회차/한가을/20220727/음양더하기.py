# 어떤 정수들이 있다. 이 정수들의 절댓값을 차례대로 담은
# 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은
# 불리언 배열 signs가 매개변수로 주어진다.
# 실제 정수들의 합을 구하여 return 하도록 solution 함수 작성

def solution(absolutes, signs):
    # signs가 참이면 해당 absolutes의 수가 양수
    # 거짓이면 음수
    # 주어진 수 하나씩 접근
    # 양수, 음수가 적용된 실제 합
    answer = 0

    for x, y in zip(absolutes, signs):
        if y == True:
            answer += x
        elif y == False:
            answer -= x
    return answer