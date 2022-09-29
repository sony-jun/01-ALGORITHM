import sys
input = sys.stdin.readline
t = map(int, input().split())

#set함수를 이용하여 집합 a, b를 만든다.
a = set(map(int, input().split()))
b = set(map(int, input().split()))

#a-b b-a를 더한 값을 구하여 출력한다.
result = (len(a-b)+len(b-a))
print(result)