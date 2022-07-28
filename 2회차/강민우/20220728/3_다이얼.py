N = input()
number = {
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ' : 9
}
total = 0

for alp in N :
    for num in number :
        if alp in num :
            total += number.get(num) +1

print(total)

