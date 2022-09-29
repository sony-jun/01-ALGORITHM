sen = input()
condition = ['none', 'unsure', 'happy', 'sad']
happy = sen.count(':-)')
sad = sen.count(':-(')
if happy == 0 and sad == 0:
    print(condition[0])
elif happy == sad:
    print(condition[1])
elif happy > sad:
    print(condition[2])
else:
    print(condition[3])