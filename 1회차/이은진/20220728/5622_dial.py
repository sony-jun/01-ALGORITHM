def trans(a):
    if (str(a) == 'A') or (str(a) == 'B') or (str(a) == 'C'):
        return '2'
    elif (str(a) == 'D') or (str(a) == 'E') or (str(a) == 'F'):
        return '3'
    elif (str(a) == 'G') or (str(a) == 'H') or (str(a) == 'I'):
        return '4'
    elif (str(a) == 'J') or (str(a) == 'K') or (str(a) == 'L'):
        return '5'
    elif (str(a) == 'M') or (str(a) == 'N') or (str(a) == 'O'):
        return '6'
    elif (str(a) == 'P') or (str(a) == 'Q') or (str(a) == 'R') or (str(a) == 'S'):
        return '7'
    elif (str(a) == 'T') or (str(a) == 'U') or (str(a) == 'V'):
        return '8'
    else:
        return '9'

word = input().upper()
numbers = ''
for w in word:
    numbers += trans(w)

total = 0
for n in numbers:
    total += int(n) + 1

print(total)