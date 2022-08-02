s = "2three45sixseven"

def solution(s):
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(en)):
        s = s.replace(en[i], str(i)) # replace() argument 2 must be str, not int
    return int(s)


print(solution(s))