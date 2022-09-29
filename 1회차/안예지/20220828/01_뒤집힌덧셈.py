# 1357

"""
"""
import sys
sys.stdin = open("뒤집힌덧셈.txt")

X, Y = input().split()
X , Y = X[::-1], Y[::-1]
words = [X, Y]
print(int(str(sum(map(int, words)))[::-1]))

# X, Y = input().split()
# rev_X = ''
# rev_Y = ''

# for idx in range(len(X) - 1, -1, -1):
#     rev_X += X[idx]
#     # print(rev_X)
    
# for idx in range(len(Y) -1, -1, -1):
#     rev_Y += Y[idx]
#     # print(rev_Y)

# rev_X, rev_Y = int(rev_X), int(rev_Y)
# rev_ = str(rev_X + rev_Y)
# answer = ''
# for idx in range((len(rev_)) - 1, -1, -1):
#     answer  += rev_[idx]
# print(int(answer))