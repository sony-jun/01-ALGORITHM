import sys
sys.stdin = open("03_괄호.txt", 'r')
'''
T = int(sys.stdin.readline())

for test_case in range(T):
    ps = sys.stdin.readline().rstrip()
    while 1:
        if len(ps) % 2 == 0:
            ps = ps.replace("()",'')
            if '(' in ps and ')' in ps:
                continue
            elif len(ps) == 0:
                print("Yes")
                break
            else:
                print("No")
                break
        else:
            print("No")
            break
'''
T = int(sys.stdin.readline())

for test_case in range(T):
    ps = list(sys.stdin.readline().rstrip())
    
    balance = 0
    ref = True
    
    if len(ps) % 2 != 0 or ps[-1] != ')':
        ref = False
    else:
        for _ in range(len(ps)):
            if ps[-1] == ')':
                ps.pop()
                balance += 1
            else:
                ps.pop()
                balance -= 1
                if balance < 0:
                    ref = False
                    break
        if balance != 0:
            ref = False
    if ref:
        print("YES")
    else:
        print("NO")