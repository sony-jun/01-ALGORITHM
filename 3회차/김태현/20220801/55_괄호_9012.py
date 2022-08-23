import sys
sys.stdin = open("55_괄호_9012.txt", "r")

# while, replace

T = int(input())

for i in range(T):
    vps = input()
    
    while "()" in vps:
        vps = vps.replace("()", "")
    
    if vps:
        print("NO")
    else:
        print("YES")