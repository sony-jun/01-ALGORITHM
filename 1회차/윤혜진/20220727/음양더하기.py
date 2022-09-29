# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 프로그래머스 문제.음양 더하기



# 함수의 인자
'''
1. 정수의 절댓값을 차례대로 담은 정수 배열 absolutes, 정수들의 부호를 차례대로 담은 불리언 배열 signs
- 1 <= absolutes의 길이 <= 1,000
- 1 <= absolutes 정수 <= 1,000
- 1 <= signs의 길이 <= 1,000
- signs[i]가 True이면 양수, False이면 음수
'''



# 함수의 반환값
'''
1. 실제 정수들의 합을 구해서 반환
'''



# 코드
def solution(absolutes, signs):
    answer = 0
    # 인덱스로 absolutes와 signs 리스트에 동시에 접근
    # absolutes의 각 절댓값에 부호를 붙인 후 합하기
    for i in range(0, len(absolutes)):
        # 부호가 음수(False)인 경우
        if not signs[i]:
            answer += -absolutes[i]
            continue
        # 부호사 양수(True)인 경우
        answer += absolutes[i]
    return answer

absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))