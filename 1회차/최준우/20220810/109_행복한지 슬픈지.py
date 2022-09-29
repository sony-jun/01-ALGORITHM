# https://www.acmicpc.net/problem/10769

sentence = input()
happy = sentence.count(':-)')
sad = sentence.count(':-(')

if happy == 0 and sad == 0:
    print('none')
else:
    if happy > sad:
        print('happy')
    elif sad > happy:
        print('sad')
    else:
        print('unsure')