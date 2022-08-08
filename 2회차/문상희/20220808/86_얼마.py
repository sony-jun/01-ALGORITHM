test_case = int(input())
for test in range(test_case):
    base = int(input())
    opt_cnt = int(input())
    opt_price = 0
    for _ in range(opt_cnt):
        opt = list(map(int, input().split()))
        opt_price += opt[0] * opt[1]
    fin = base + opt_price
    print(fin)