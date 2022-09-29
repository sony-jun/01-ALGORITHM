import sys
sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1,T+1):
    r,e,c = map(int,input().split())
    if r < e - c:
        result ='advertise'
    if r > e - c:
        result ='do not advertise'
    if r == e - c:
        result ='does not matter'
    # print(r,e-c,result)
    print(result)