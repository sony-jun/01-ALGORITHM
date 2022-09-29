# 23253.
import sys
sys.stdin = open("자료구조.txt")

N, M = map(int, input().split())
answer = "Yes"

for merge in range(M):
    i = int(input())
    stack = input().split()
    
    for books in range(i):
        number = int(stack.pop())
        
        if len(stack) != 0:
            if int(stack[-1]) < number:
                answer = "No"
                break
    if answer == "No":
        break

print(answer)