#https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
   
    list_ = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = s
    for i in range(len(list_)):
        if list_[i] in s:
            answer = answer.replace(list_[i], str(list_.index(list_[i])))
       
        
    return answer

print(solution('one4seveneight'))
print(solution('23four5six7'))
print(solution('2three45sixseven'))
print(solution('123'))
