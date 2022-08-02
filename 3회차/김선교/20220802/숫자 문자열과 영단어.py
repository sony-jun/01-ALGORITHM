numbers = {
'zero'  :0,
'one'   :1,	
'two'   :2,	
'three' :3,	
'four'  :4,	
'five'  :5,	
'six'   :6,	
'seven' :7,
'eight' :8,
'nine'  :9}

def solution(s):
    answer = ''
    heap = ''
    s = list(s)[::-1]
    while len(s):
        if s[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '8', '0']:
            answer += s.pop()
        else:
            heap += s.pop()
        if heap in numbers:
            answer += str(numbers[heap])
            heap = ''
    return int(answer)