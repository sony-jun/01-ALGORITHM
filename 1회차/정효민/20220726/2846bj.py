
T = int(input())
for test_case in range(1 , T + 1):
    result = []

    a , b ,c ,d ,e= map(int , input().split())
    all = [a , b , c , d ,e]
    for i in range(len(all)):
        for i2 in range(i + 1 ,len(all)):
            if all[i] < all[i2]:
                result.append(all[i])
    print(set(result))