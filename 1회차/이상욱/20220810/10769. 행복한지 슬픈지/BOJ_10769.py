import sys
sys.stdin = open('10769.txt')

word = input()

happy = word.count(':-)')
sad = word.count(':-(')

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == 0 and sad == 0:
    print('none')
else:
    print('unsure')