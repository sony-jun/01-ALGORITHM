#직사각형의 네개의 합집합의 면적구하기
# 입력 4줄 
# 겹치는 면적은 뺀다.
import sys
sys.stdin = open('면적구하기.txt','r')

paper = [[0 for _ in range(101)] for _ in range(101)]
li=[]
for _ in range(4):
    x1,y1,x2,y2 = list(map(int,input().split()))
    
    for i in range(x1,x2):
        for j in range(y1,y2):
            paper[i][j] = 1
result = 0 
for n in paper:
    result += sum(n)
print(result)
