# dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
#         'four': '4', 'five': '5', 'six': '6', 'seven': '7',
#         'eight': '8', 'nine': '9'}
# str = input()

# for key, value in dict.items():
#     str = str.replace(key, value)

# print(int(str))


def solution(s):
    answer = s
    dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'}
    
    for key, value in dict.items():
        answer = answer.replace(key, value)

    return int(answer)