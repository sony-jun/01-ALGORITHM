# 0<=n<=99
# if n<10: print(f'0{n}'),
x = int(input())
c = 0
n = x
# n = ab
# a + b = cd
# n = bd
while True:
    sn = str(n)
    # print(n,type(n))
    if n < 10:
        sn = '0'+ sn  # a = 0, b = n
    # print(sn)
    s = int(sn[0]) + int(sn[1]) # s = int # cd  
    sl = str(s) # sl = str
    # print(sl)
    if s<10:
        sl = '0'+sl # c=0 d = sl
    n = sn[1]+sl[1] # n = int  # bd
    n = int(n)
    # print(n)
    c += 1
    if n == x:
        break
print(c)