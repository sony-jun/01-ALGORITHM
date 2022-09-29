# https://www.acmicpc.net/problem/10769
import sys
sys.stdin = open('B10769.txt')

msg = input()
happy = msg.count(':-)')
sad = msg.count(':-(')
if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')