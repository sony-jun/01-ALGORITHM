from re import A
import sys

sys.stdin = open("06_A+B-3.txt")

T = int(input())

for i in range(T):
    a,b = map(int, input().split())
    print(a+b)

#아, 이제 이해했다..테스트케이스의 갯수 T가 주어진다.
# 그 T의 갯수는 TXT파일 위에있는 5<<5개라는거고!
# input으로 받아서.for 문으로 그 테스트케이스 갯수만큼 반복해라.
