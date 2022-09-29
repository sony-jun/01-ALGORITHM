for _ in range(int(input())):
    sum = 0
    
    A, B = map(int, input().split())

    if A == 1:
        sum += 5000000
    elif 1 < A <= 3:
        sum += 3000000
    elif 3 < A <= 6:
        sum += 2000000
    elif 6 < A <= 10:
        sum += 500000
    elif 10 < A <= 15:
        sum += 300000
    elif 15 < A <= 21:
        sum += 100000
    else:
        sum += 0


    if B == 1:
        sum += 5120000
    elif 1< B <= 3:
        sum += 2560000
    elif 3 < B <= 7:
        sum += 1280000
    elif 7 < B <= 15:
        sum += 640000
    elif 15 < B <= 31:
        sum += 320000
    else:
        sum += 0

    print(sum)



# contest_A = [1, 3, 6, 10, 15, 21]
# contest_AM = [500, 300, 200, 50, 30, 10]
# contest_B = [1, 3, 7, 15, 31]
# contest_BM = [512, 256, 128, 64, 32]

# for _ in range(int(input())):
#     상금A = []
#     상금B = []

#     A, B = map(int, input().split())
#     for con_A in contest_A:
#         if A > 21 or A == 0:
#             상금A = [0]
#         elif A <= con_A:
#             상금A.append(contest_AM[contest_A.index(con_A)])

#     for con_B in contest_B:
#         if B > 31 or B == 0:
#             상금B = [0]
#         elif B <= con_B:
#             상금B.append(contest_BM[contest_B.index(con_B)])

#     print((max(상금A) + max(상금B))* 10000)