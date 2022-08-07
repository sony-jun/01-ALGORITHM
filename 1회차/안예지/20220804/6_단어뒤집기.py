# 9093.
""" 
"""
import sys
sys.stdin = open("단어뒤집기.txt")
T = int(input())

for _ in range(T):
    sentence = ''
    words = input().split()
    for chr in words:
        sentence += chr[::-1] + ' '
    print(sentence)        
        