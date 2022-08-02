#프로그래머스

def solution(s):

    word = s
    dic_ = { '0' : 'zero', '1' : 'one', '2'	: 'two', '3' : 'three', '4'	: 'four', '5' : 'five', '6'	: 'six', '7' : 'seven', '8'	: 'eight', '9' : 'nine'
    }

    for key, value in dic_.items():  #여기서부터 구글링 key값만 어떻게 출력하는지 모르겠어서,,
        #items는 key와 value를 튜플로 묶은 값
        word = word.replace(value, key)
    
    return int(word)
    
