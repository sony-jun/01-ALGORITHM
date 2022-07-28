import sys
sys.stdin = open('1357.txt')

T = int(input())

for i in range(1, T+1):
    X, Y = input().split() 

    Rev_X = (int(X[::-1])) 
    Rev_Y = (int(Y[::-1])) 

    print(str(Rev_X + Rev_Y)[::-1]) 