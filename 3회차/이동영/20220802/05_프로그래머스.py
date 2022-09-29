def solution(s):
    dict_ = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    s = str(s)
    for i in list(dict_.keys()):
        if i in s:
            s = s.replace(i, str(dict_[i]))
       
    return int(s)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution(123))