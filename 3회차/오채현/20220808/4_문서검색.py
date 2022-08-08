# doct = input()
# ser = input()

doct = 'ababababa'
ser = 'aba'

cnt = 0
n = 0
while n <= len(doct) - len(ser):
    if doct[n:n+len(ser)] == ser:
        cnt += 1
        n += len(ser)
    else:
        n += 1
print(cnt)
