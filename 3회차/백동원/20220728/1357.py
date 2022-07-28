# 뒤집힌 덧셈

def Rev(A):                         # 정수형 변수 A를 인풋으로 하는 함수 작성
    str_number = ''                 
    while A != 0:                   
        str_number += str(A % 10)   # 입력값을 10으로 나눈 나머지를 문자열로 바꿔 빈 문자열에 더한다.
        A //= 10                    # 반복문이 종료됬을 때는 입력값을 뒤집은 값이 문자열로 str_number에 할당된다.
    return int(str_number)          # str_number를 정수형으로 변환하면서 앞자리가 0인 부분을 떼어내고, 출력한다.

X, Y = map(int, input().split())    
print(Rev(Rev(X) + Rev(Y)))         # 문제에서 요구한대로 함수를 활용해준다.