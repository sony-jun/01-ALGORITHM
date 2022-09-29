from pprint import pprint
import sys

x,y = map(int,input().split(' '))

input = sys.stdin.readline

sublist = []
for i in range(x):
    sublist.append(input().split())

opplist = []
for lst in sublist:
    slst = lst.reverse()
    print(slst)
    opplist.append(slst)

pprint(sublist)
pprint(opplist)