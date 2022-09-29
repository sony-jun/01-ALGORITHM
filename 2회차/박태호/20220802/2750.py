
import sys 

sys.stdin = open('2750.txt','r')

# n = int(input())
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    # num = int(input())
    num = int(sys.stdin.readline())
    li.append(num)
li.sort()
print(*li,sep='\n')
 