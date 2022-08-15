emoji = input()

happy = emoji.count(':-)')
sad = emoji.count(':-(')

if sad != 0 or happy != 0 :
    if sad == happy :
        print('unsure')

    elif sad > happy :
        print('sad')

    elif sad < happy :
        print('happy')  

else :
    print('none')