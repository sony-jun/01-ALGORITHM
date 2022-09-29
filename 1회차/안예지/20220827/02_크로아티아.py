# 2941
"""
"""
import sys
sys.stdin = open("크로아티아알파벳.txt")

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()
for alpha in croa:
     if alpha in words:
         words = words.replace(alpha, "*")

print(len(words))

    
    