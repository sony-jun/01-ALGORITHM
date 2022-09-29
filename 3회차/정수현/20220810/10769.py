text = input()
nHappy = text.count(':-)')
nSad = text.count(':-(')
if nHappy == nSad:
    print('unsure')
elif nHappy > nSad:
    print('happy')
elif nHappy < nSad:
    print('sad')
else:
    print('none')