sentence = input()
if ':-)' not in sentence and ':-(' not in sentence:
    print('none')
else:
    if sentence.count(':-)') == sentence.count(':-('):
        print('unsure')
    elif sentence.count(':-)') > sentence.count(':-('):
        print('happy')
    else:
        print('sad')