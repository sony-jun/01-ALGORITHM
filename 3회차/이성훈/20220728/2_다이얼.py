# https://www.acmicpc.net/problem/5622
import sys

sys.stdin = open("2_다이얼.txt")

T = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

input_ = input()
list_ = []

for i in T:
    for j in range(len(input_)):
        if input_[j] in i:          # if input_[0] in 'ABC' 
            list_.append(T.index(i)+3)      
            
print(sum(list_))
    
