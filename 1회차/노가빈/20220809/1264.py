while True:
    str = input()
    if str == '#':
        break
    result = str.count('a')+str.count('e')+str.count('i')+str.count('o')+str.count('u')
    result += str.count('A')+str.count('E')+str.count('I')+str.count('O')+str.count('U')
    print(result)