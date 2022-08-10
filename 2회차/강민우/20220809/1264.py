
alp = ['a','e','i','o','u']


while True:
    N = input().split()
    for t in N:
        cnt = 0
        for s in alp:
            t.replace(s,'@')
            cnt += t.count('@')
        print(cnt)
    if N == ['#']:
        break