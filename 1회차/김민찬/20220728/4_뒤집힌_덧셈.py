X, Y = map(str, input().split()) # 문자열로 입력 받는다.

sum = str(int(X[::-1]) + int(Y[::-1])) # int형으로 변환한다. # 더해주고 str형으로 다시 변환
# sum = (int(X[::-1] + int(Y[::-1]))) # TypeError: can only concatenate str (not "int") to str

print(sum[::-1])
# print(int(sum[::-1])) # 뒤집은 값을 정수형으로 변환