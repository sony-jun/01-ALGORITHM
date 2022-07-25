n = int(input())
n1 = n
mok = 0
namo = 0
m_n_sum = 0
cnt=0
while 1:
    mok = n//10
    namo = n%10
    m_n_sum = mok+namo
    n = namo*10+m_n_sum%10
    cnt+=1
    if n==n1:
        print(cnt)
        break