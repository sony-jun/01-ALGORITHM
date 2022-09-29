T = input()

zankyo = T.split('(^0^)')

for idx in zankyo:
    print(idx.count('@'), end=' ')