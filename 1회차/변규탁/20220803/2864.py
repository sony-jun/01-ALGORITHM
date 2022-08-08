# A, B = map(str, input().split())

# answer_min = int(A.replace('6','5')) + int(B.replace('6', '5'))
# answer_max = int(A.replace('5','6')) + int(B.replace('5', '6'))


# print(answer_min, answer_max)





'''
>문제조건 
상근이가 2863번 5 6 헷갈린다 
5를 6로 볼때도 있고 6을 5로 볼때도 있다 -> 코드

>아이디어
5는 6으로
6은 5로 --> replace 

>조건세분화 

min_ =  
max_ =
'''


# min_ = int(A.replace('6', '5')) + int(B.replace('6', '5')) 
# max_ = int(A.replace('5', '6')) + int(B.replace('5', '6'))

# print(min_, max_)


def solution(A, B):
    
    min_ = int(A.replace('6', '5')) + int(B.replace('6', '5')) 
    max_ = int(A.replace('5', '6')) + int(B.replace('5', '6'))

    answer1, answer2 = min_, max_
    return answer1, answer2
     

A, B = input().split()

ans1, ans2 = solution(A, B)
print(ans1, ans2)