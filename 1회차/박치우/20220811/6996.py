import sys
sys.stdin = open('6996.txt')

test_case = int(input())
for i in range(test_case):
    A, B = input().split()
    dic_A = dict()
    dic_B = dict()
    for j in A:
        if j in dic_A:
            dic_A[j] += 1
        else:
            dic_A[j] = 1
    for k in B:
        if k in dic_B:
            dic_B[k] += 1
        else:
            dic_B[k] = 1
    
    if dic_A == dic_B:
        print(A,'&',B,'are anagrams.')
    else:
        print(A,'&',B,'are NOT anagrams.')
