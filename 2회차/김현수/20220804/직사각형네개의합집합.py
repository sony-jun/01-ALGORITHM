import sys
sys.stdin = open('직사각형네개의합집합.txt') 
from pprint import pprint

square = [list(map(int,input().split())) for _ in range(4)]
pprint(square) #[x,y,x_,y_]
sum_ = []
for _ in range(4):
    for a in range(square[_][0],square[_][2]):
        for b in range(square[_][1],square[_][3]):
            sum_.append((a,b))

answer = len(list(set(sum_)))
print(answer)