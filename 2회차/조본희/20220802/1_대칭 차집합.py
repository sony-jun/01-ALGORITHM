import sys
input = sys.stdin.readline

A, B = map(int, input().split())

numbersA = set(map(int, input().split()))
numbersB = set(map(int, input().split()))

print(len(numbersA - numbersB) + len(numbersB - numbersA))