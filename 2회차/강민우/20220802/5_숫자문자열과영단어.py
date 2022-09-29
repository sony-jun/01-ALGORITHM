
def solution(s):
    number = {}
    numbers = ['zero' , 'one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine']
    i = 0
    for a in numbers :
        number[a] = number.get(a,0) + i
        i += 1
    for a in numbers:
        s = s.replace(a , str(number[a]))
    answer = int(s)
    return answer
