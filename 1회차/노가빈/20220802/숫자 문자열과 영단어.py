
numList = ['0','1','2','3','4','5','6','7','8','9']
strList = ['zero','one','two','three','four','five','six','seven','eight','nine']

def solution(str):
    
    for i in range(10):
        if strList[i] in str:
            str = str.replace(strList[i],numList[i])
    return int(str)

print(solution('one4seveneight'))
print(solution('23four5six7'))
print(solution('2three45sixseven'))
print(solution('123'))
