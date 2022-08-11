import sys
sys.stdin = open('17388.txt')

S, K, H = (map(int, sys.stdin.readline().split()))
total = S+K+H

if total >= 100:
    print('OK')
else:
    if min(S,K,H)==S:
        print('Soongsil')
    elif min(S,K,H)==K:
        print('Korea')
    else:
        print('Hanyang')