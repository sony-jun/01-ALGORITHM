import sys

sys.stdin = open('문서 검색.txt')

M = input()
N = input()

M=M.replace(N, '-')

result = 0

for i in M:
    if i == '-':
        result +=1
    
print(result)

                



