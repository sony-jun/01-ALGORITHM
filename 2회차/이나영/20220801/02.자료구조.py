from re import A
import sys

sys.stdin = open("02.자료구조.txt")


sys.stdin.readline()

stack_list= []
answer = "Yes"

for stack in stack_list:
    comparison = stack.pop()
    while len(stack) != 0:
        comparison = stack.pop()
    else:
        answer
