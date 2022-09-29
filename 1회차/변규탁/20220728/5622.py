dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# 3초, 4초 ~~~~~~~~~~~12초

word = input()
second = 0
for char in word:
    for dial in dials:
        if char in dial:
            second += 3 + dials.index(dial)
print(second)