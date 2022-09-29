import sys

sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    money = list(map(int, input().split()))

    if money[0] < money[1] - money[2]:
        print('advertise')
    
    elif money[0] == money[1] - money[2]:
        print('does not matter')

    elif money[0] > money[1] - money[2]:
        print('do not advertise')