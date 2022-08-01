X, Y = map(str, input().split()) #문자열로 입력 받기
# 문자열로 입력받은 값을 뒤집고 int로 변환한 다음
# 더한 후에 다시 문자열로 바꾼다.
rev = str(int((X)[::-1]) + int((Y)[::-1]))

print(int(rev[::-1])) #다시 뒤집은 다음 int로 변환해준다.

#def함수 이용하기
#매개변수를 숫자로 이루어진 문자열X로
def rev(X): 
    X = int(X[::-1]) #X를 뒤집고 정수형으로 바꾼다
    return X

X,Y = input().split()
#rev(X) + rev(Y)는 정수형이고 rev함수는 문자열을 받기 때문에
#문자열로 바꾸어 준다.
re = rev(str(rev(X) + rev(Y)))
print(re)