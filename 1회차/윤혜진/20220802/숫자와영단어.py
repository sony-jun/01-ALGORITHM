# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 2021 카카오 채용연계 인턴십 문제.숫자 문자열과 영단어
# 시간제한: 10초



# 함수의 매개변수
'''
1. 문자열 s
- s: 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 바뀌지 않고 그대로임
- 1 <= s의 길이 <= 50
- s가 'zero' 또는 '0'으로 시작하는 경우는 없음
'''



# 함수의 반환값
'''
1. 문자열 s가 의미하는 원래 숫자를 반환
'''



# 코드
def solution(s):
    answer = s
    english = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    # 숫자 영단어를 숫자로 변환
    for en in english:
        answer = answer.replace(en, english[en])
            
    return answer



print(solution('one4seveneight'))