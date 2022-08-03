# https://www.acmicpc.net/problem/2167

import sys
sys.stdin = open('2.txt', 'r')
from pprint import pprint

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
k = int(input())
sum_ = []

for i in range(k):
    i, j, x, y = map(int,input().split())
    




