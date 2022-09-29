T = int(input())

for _ in range(T):
    A, B = input().split()
    
    a = sorted(list(A))
    b = sorted(list(B))

    if a == b:
        print("{} & {} are anagrams.".format(A, B))
    else:
        print("{} & {} are NOT anagrams.".format(A, B))



    # cnt = 0
    # for word in A:
    #     if word in B:
    #         cnt += 1
    # if len(A) == len(B) and cnt == len(A):
    #     print("{} & {} are anagrams.".format(A, B))
    # else:
    #     print("{} & {} are NOT anagrams.".format(A, B))