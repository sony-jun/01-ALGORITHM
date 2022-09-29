import sys
sys.stdin = open('B7785.txt')

n = int(input())
list = {}
for i in range(n):
    name, log = input().split()
    if log == 'enter':
        list[name]='1'