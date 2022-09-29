import sys
sys.stdin = open('대칭자집합.txt', 'r')

A, B = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

print((a|b) - (a&b))

#set함수 더하기 뺴기