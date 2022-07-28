# 숫자가 뒤집히는 함수
def rev(n):
    return int(str(n)[::-1])

x, y = map(int, input().split())
# x 뒤집기
x_rev = rev(x)
# y 뒤집기
y_rev = rev(y)
# x_rev와 y_rev 더하기
sum = x_rev + y_rev

# sum 뒤집기
print(rev(sum))