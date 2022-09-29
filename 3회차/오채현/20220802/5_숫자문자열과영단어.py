# def solution(s):
#     words = {
#         'zero': '0', 
#         'one': '1', 
#         'two': '2',
#         'three': '3',
#         'four': '4',
#         'five': '5',
#         'six': '6',
#         'seven': '7',
#         'eight': '8',
#         'nine': '9'
#     }
#     answer = s
#     for word in words.items():
#         answer = answer.replace(word[0], word[1])

        # for k, v in words.items():
        #     s = s.replace(k, v)

#     return int(answer)


# print(solution('one4seveneight'))

#리스트 인덱스 번호로 해도 될 듯

def solution(s):
    words = [
        'zero', 
        'one', 
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]
        
    answer = s
    
    for word in words:
        if word in answer:
            answer = answer.replace(word, str(words.index(word)))

    return int(answer)

print(solution('one4seveneight'))
