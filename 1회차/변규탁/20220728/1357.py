X, Y = map(int, input().split())

reverse_num_X = ''
while X != 0:
    reverse_num_X += str(X % 10)
    X = X // 10

reverse_num_Y = ''
while Y != 0:
    reverse_num_Y += str(Y % 10)
    Y = Y // 10

sum_ = int(reverse_num_X) + int(reverse_num_Y)

answer = ''
while sum_ != 0:
    answer += str(sum_ % 10)
    sum_ = sum_ // 10

print(int(answer))