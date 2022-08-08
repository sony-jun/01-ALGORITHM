from re import L
import sys
sys.stdin = open("2_영화감독숌.txt" ,'r')

N = int(sys.stdin.readline())
title = set()

for i in range(N):
    for j in range(N):
        title.add(int(str(i) + '666'))
        title.add(int('666' + str(j)))
        title.add(int(str(i) + '666' + str(j)))
title = sorted(list(title))
del title[N:]
print(title.index())
print(title[N-1])