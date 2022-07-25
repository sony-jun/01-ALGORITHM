# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(sys.stdin.readline())               
b = int(sys.stdin.readline())                
c = int(sys.stdin.readline())       

result = list(str(a * b * c))   

for i in range(10):            
    print(result.count(str(i))) 