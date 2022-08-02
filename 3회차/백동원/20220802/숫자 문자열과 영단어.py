def solution(s):
    word = ''
    result = ''
    numbers = {                         # 딕셔너리 작성
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
    for spell in s:                     # 입력값을 하나씩 순회
        word += spell                   # word라는 빈 문자열에 하나씩 더함
        if word in numbers.keys():      # 더해나가다가 딕셔너리의 키 값들 중 일치하는 키가 있을 경우
            result += numbers[word]     # result라는 빈 문자열에 해당하는 키의 값을 더하고
            word = ''                   # word는 다시 초기화
        elif spell in numbers.values(): # 순회 도중 value 값들 중 일치하는 것이 있을 경우
            result += spell             # result에 그 값을 더하고  
            word = ''                   # word 값은 다시 초기화
    answer = int(result)                # 결과를 정수형으로 변환 후 반환
    return answer