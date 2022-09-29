import sys
sys.stdin = open('17388.txt')

score = list(map(int, sys.stdin.readline().split()))
total = sum(score)

if total >= 100:
    print('OK')
else:
    if score.index(min(score)) == 0:
        print('Soongsil')
    elif score.index(min(score)) == 1:
        print('Korea')
    elif score.index(min(score)) == 2:
        print('Hanyang')
