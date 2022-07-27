# 76501.
"""
어떤 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와
이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수
실제 정수들의 합을 구하여 return

# 입력
signs의 길이와 같은 aboslutes 배열이 주어진다.
signs[i]가 참이면 aboslutes[i]의 실제 정수가 양수,
그렇지 않으면 음수임을 의미한다.

# 출력
실제 정수들의 합

# 접근
1. 처음부터 배열로 주어지니까 인덱스로 접근해야겠다.
2. 불리언 배열이므로 값은 true는 1, flase는 0
3. 실제 정수의 합을 구하는 거니까 양수면 더하고,
4. 음수면 빼자.

"""
def solution(absolutes, signs):
    answer = 0
    for idx in range(len(signs)):
        # 길이가 같다는 것은 같은 인덱스를 공유한다
        if signs[idx] == 1:
            # 불리언 배열이므로 true의 값은 1
             answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
            
    return answer