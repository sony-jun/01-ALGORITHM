number = str(input())

while set(number) != {'4', '7'} and set(number) != {'4'} and set(number) != {'7'}:
    for i in number:
        if i != '4' and i != '7':
            number = int(number)
            number -= 1
            number = str(number)

print(number)