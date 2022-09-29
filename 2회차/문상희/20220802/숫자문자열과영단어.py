def solution(s):
    answer = s
    number = {
        'zero'  : '0',
        'one'   : '1',
        'two'   : '2',
        'three' : '3',
        'four'  : '4',
        'five'  : '5',
        'six'   : '6',
        'seven' : '7',
        'eight' : '8',
        'nine'  : '9'
    }

    for i in number:
        answer = answer.replace(i, number[i])
        # 딕셔너리로 키- 밸류값 지정하여 replace 매서드 이용해 변환
    return int(answer)