# solution 정의
def solution(s):
    answer = ''
    dic = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }

    answer = s
    # dic의 아이템에 있는 키와 값을 처음부터 끝까지 돌아서 꺼냄
    for key, value in dic.items():
        # answer의 키에 맞는 값을 대체함
        answer = answer.replace(key, value)
    # answer에 int 형변환해서 반환
    return int(answer)


# Programmers 다른 사람의 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)