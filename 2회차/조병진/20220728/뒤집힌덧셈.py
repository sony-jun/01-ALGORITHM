# 뒤집힌 덧셈
# 문제 : 두 양의 정수 X와 Y가 주어졌을 때,
#       Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오
# 접근 : 문자열로 입력받아 뒤집어서 더하고, 다시 뒤집기

x, y = input().split()

x_rev = x[::-1]
y_rev = y[::-1]

sum_ = str(int(x_rev) + int(y_rev))
print(int(sum_[::-1]))
