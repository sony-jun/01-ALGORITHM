# 프로그래머스 숫자 문자열과 영단어

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"

# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 
# 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

def solution(s):

    dict = {
    'zero': 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 
    'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9
    }
    
    # items() 부르면 딕셔너리에서 (키, 밸류)가 튜플형태로 한번에 둘이 들어온다.
    # ["zero", 2] , ["one", 1]... 이런식으로
    for d in dict.items():
        # 문자열.replace("검색 문자", "치환 문자", 치환 횟수)
        # answer 가 문자열로 들어오니까 치환도 문자열로 해준다.
        s = s.replace(d[0], str(d[1]))
    
    # 마지막에 문자열인 answer를 한번에 형변환해준다.
    return int(s)

