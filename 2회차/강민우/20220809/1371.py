import sys

sys.stdin = open('input.txt')
N =  sys.stdin.read().replace('\n', '').replace(' ','')
alp = {}
N = list(N)

for a in N:
    alp[a] = alp.get(a,0) + 1

alps = sorted(alp.keys())
for a in alps:
    if alp[a] == max(alp.values()):
        print(a,end = '')
