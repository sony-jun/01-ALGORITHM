def re_verse(number):
    lst = []
    number = str(number)
    for num in number:
        lst.append(num)
    lst.reverse()
    number = ''.join(lst)
    number= int(number)
    return number
    
a, b = input().split()
a = int(a)
b = int(b)
sum = re_verse(a) + re_verse(b)
print(re_verse(sum))



