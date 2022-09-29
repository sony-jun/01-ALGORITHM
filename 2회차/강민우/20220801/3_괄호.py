T = int(input())

for test_case in range(T):
    N = list(input())
    total = {
        ')' : 0,
        '(' : 0
        }
    for a in N :
        total[a] +=  1
        if N[0]  == ')' or len(N)%2 !=0:
            break
        
        if total.get('(') < total.get(')'):
            break
    if total.get('(') == total.get(')'):
       print('YES')
    else:
        print('NO')