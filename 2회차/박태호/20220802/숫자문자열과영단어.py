
# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나,
#  혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
#  s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

def solution(s): # "one4seveneight"
    ch = [
        'zero','one','two','three','four',
        'five','six','seven','eight','nine'
    ] 
    for i in range(len(ch)):                 # 인덱스로 접근예정
        if ch[i] in s:                       # 입력받은 문자열에 'one'이런게 있다면
            answer = s.replace(ch[i],str(i)) # 문자를 품은 인덱스로 
            s = answer                       # 반복할 s를 바꿔야 한다.
    # answer = s.replace('one','1')
    return int(s) # 숫자로 출력
print(solution('one4seveneight')) #  '14seveneight' 'one47eight'