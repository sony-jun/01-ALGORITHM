# 주어진 두 수를 뒤집고 더 한 다음 뒤집은 값을 출력


# x, y = input().split()

# x = int(x[::-1]) #123 -> 321
# y = int(y[::-1]) #100 -> 1
# #print(x,y) #321,1 

# rev = x + y  #322
# rev_li = str(rev) #str로 변환하여 list만들기

# print((int(rev_li[::-1]))) #다시 int로 변환해서 추출

# X, Y = map(int, input().split())

rev_x = 0
while True:
    if X < 10:
        rev_x = X
        break
    rev_x += X % 10
    X = X // 10
    rev_x *= 10
    if X < 10:
        rev_x += X
        break
#print(rev_x)
rev_y = 0
while True:
    if Y < 10:
        rev_y = Y
        break
    rev_y += Y % 10
    Y = Y // 10
    rev_y *= 10
    if Y < 10:
        rev_y += Y
        break
#print(rev_y)
sum_ = rev_x + rev_y
ans = 0
while True:
    if sum_ < 10:
        ans += sum_
        break
    ans += sum_ % 10
    sum_ = sum_ // 10
    ans *= 10
    if sum_ < 10:
        ans += sum_
        break
print(ans)
#====================================
# def Rev(n):
#     return int(str(n)[::-1])

# n1, n2 = map(int, input().split())
# print(Rev(Rev(n1) + Rev(n2)))