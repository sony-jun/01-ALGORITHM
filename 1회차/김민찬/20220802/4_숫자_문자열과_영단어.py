import sys

sys.stdin = open("4_숫자_문자열과_영단어.txt")

def solution(W): # 문자 -> 숫자 / 딕셔너리 정의
    dic = { 'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4',
            'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'
    }
    
    for i in dic:
        W = W.replace(i, str(dic[i])) # 문자열을 딕셔너리 값으로 변환
    
    return int(W) # int화 해서 return