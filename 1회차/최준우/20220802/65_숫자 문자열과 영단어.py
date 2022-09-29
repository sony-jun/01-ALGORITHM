# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ''
    temp = ''
    my_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
    }
    
    for char in s:
        temp += char
        if temp in my_dict:
            answer += my_dict[temp]
            temp = ''
            
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))