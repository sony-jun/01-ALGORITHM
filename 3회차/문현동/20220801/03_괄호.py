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
# ()))((()
for test_case in range(T):
    ps = list(sys.stdin.readline().rstrip())
    
    left = 0
    right = 0
    
    if len(ps) % 2 != 0 or ps[-1] != ')':
        print("No")
        
    else:
        for _ in range(len(ps)): # ( ( ( ( ) ( ) ) ( )
            if ps.pop() == ')':
                right += 1
            else:
                left += 1
                while left < right:
                    if ps[-1] == '(':
                        ps.pop()
                        left += 1
                        continue
                    else:
                        print("No")
                        break
                if ps[-1] != ')':
                    print("No")
                    break