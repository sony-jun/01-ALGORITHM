def solution(s):
    answer = s                                      # 전달받은 문자열 s를 answer에 저장
    num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,    # key:value - 영단어:숫자
            'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for key, value in num.items():                  # num의 key, value 값에서
        answer = answer.replace(key, str(value))    # answer의 key를 value로 변경

    return int(answer)                              # answer 리턴

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))