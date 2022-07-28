# https://www.acmicpc.net/problem/1357
import sys

sys.stdin = open("4_뒤집힌 덧셈.txt")

X, Y = input().split()

def Rev(X):
    Y = int(str(X)[::-1])
    return Y


print(Rev(Rev(X) + Rev(Y)))
    
