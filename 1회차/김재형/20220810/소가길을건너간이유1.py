import sys
sys.stdin = open('소가길을건너간이유1_input.txt')

n = int(input())


#[[3, 1], [3, 0], [6, 0], [2, 1], [4, 1], [3, 0], [4, 0], [3, 1]]

dict_ = {}
road = []
for i in range(1,n):
    stack = list(map(int, input().split()))
    for j in range(2):
        if stack[i-1][0] in stack[i][0]:
            if stack[i-1][1] != stack[i][1]:
                
