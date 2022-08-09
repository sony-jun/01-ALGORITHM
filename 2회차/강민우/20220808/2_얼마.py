T = int(input())

for test_case in range(T):
    price = int(input())
    option = 0
    for n in range(int(input())):
        q,p = map(int, input().split())
        option += q*p
    
    print(price + option)