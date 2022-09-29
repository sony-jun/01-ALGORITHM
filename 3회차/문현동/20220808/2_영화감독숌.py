import sys
sys.stdin = open("2_영화감독숌.txt" ,'r')

N = int(sys.stdin.readline())
devil = {666}
i = 666

while len(devil) < N:
    i += 1
    if '666' in str(i):
        devil.add(i)
        
answer = sorted(list(devil))[N - 1]
print(answer)