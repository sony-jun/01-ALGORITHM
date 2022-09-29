# 1357번 뒤집힌 덧셈

def Rev(x):
    reverse_num = ''
    # 문자열에 있는것을 하나씩 빼서 reverse_num에 거꾸로 다시 넣어준다.
    for i in x:
        reverse_num = i + reverse_num
    
    # 결과를 숫자로 반환한다.
    return int(reverse_num)

# 첫째 줄에 수 X와 Y가 문자열 형태로 주어진다.
X, Y = input().split()
print(Rev(str(Rev(X) + Rev(Y))))