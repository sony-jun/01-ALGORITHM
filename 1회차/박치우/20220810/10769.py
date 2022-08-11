str_ = input()
smile = str_.count(':-)')
sad = str_.count(':-(')
if smile == 0 and sad == 0:
    print('none')
elif smile > sad :
    print('happy')
elif sad > smile :
    print('sad')
elif sad == smile :
    print('unsure')