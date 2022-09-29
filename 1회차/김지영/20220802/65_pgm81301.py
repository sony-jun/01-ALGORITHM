
s = input()
# print(s,type(s))
def solution(s):
    dic = { 'zero': '0','five':'5',
            'one': '1','six':'6',
            'two': '2','seven':'7',
            'three': '3','eight':'8',
            'four': '4','nine':'9'  }
    for k,v in dic.items():
        if k in s:
            # print(key,s,type(key),type(s))
            s = s.replace(k,v)
    answer = int(s)
    # print(answer,type(answer))
    return answer
print(solution(s))