# 프로그래머스

from unittest import result


eng_num_dic = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

# 1.
def solution(s):
    answer = s
    for key, value in eng_num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
# eng_num_dic.items()는 key와 value의 쌍을 튜플로 묶은 값을 리스트 형태로 돌려줌
# key, value 값이 둘 다 존재하는지 확인 가능
# eng_num_dic.items([('zero', '0'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')])

# 2.
def solution(s):
    # value를 value_list에 저장
    value_list = eng_num_dic.values()
    result = []
    temp = ''

    for i, s in enumerate(s):
        # 만약 숫자가 나오면 숫자를 result에 추가
        if s in value_list:
            result.append(s)
        # 문자가 나오면
        else:
            # 임시 문자열에 붙이다가
            temp += s
            # 임시문자열 중 eng_num_dic의 key에 같은게 있으면
            if temp in eng_num_dic:
                # value를 result에 추가
                result.append(eng_num_dic[temp])
                # temp 초기화
                temp = ''
    # 리스트 -> 문자열 -> 숫자
    return int(''.join(result))
# ''.join(리스트) -> 리스트를 문자열로 변경


# 3.
def solution(s):
    value_list = eng_num_dic.values()
    result = ''
    temp = ''

    for i, s in enumerate(s):
        if s in value_list:
            result += s
        else:
            temp += s
        if temp in eng_num_dic:
            result += eng_num_dic[temp]
            temp = ''
    return int(result)