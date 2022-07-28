import sys
sys.stdin = open("4_뒤집힌덧셈.txt", 'r')

X, Y = input().split()

rev_x = X[::-1]
rev_y = Y[::-1]

print(int(str(int(rev_x) + int(rev_y))[::-1]))