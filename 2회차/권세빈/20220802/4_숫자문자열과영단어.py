def solution(s):
    dict = {            # 딕셔너리로 값 저장
        'zero': '0',
	    'one' : '1',
	    'two' : '2',
	    'three' :'3', 
	    'four' : '4',
	    'five' : '5',
	    'six' : '6',
	    'seven' :'7', 
	    'eight' : '8',
	    'nine' : '9'
        }

    for k, v in dict.items():   # 딕셔너리의 키와 밸류 뽑기
        s = s.replace(k,v)      # 키값과 똑같은 문자열을 밸류값으로 바꾸기
    return int(s)               # 정수로 변환 후 리턴

# print(solution('one4seveneight'))
# print(solution('23four5six7'))
# print(solution('2three45sixseven'))
