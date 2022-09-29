import sys
sys.stdin = open("20220728/1357_뒤집힌덧셈.txt")

X, Y = input().split()

sum_XY = str(int(X[::-1]) + int(Y[::-1]))  
Rev_sum = int(sum_XY[::-1]) 

print(Rev_sum)