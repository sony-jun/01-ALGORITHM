K = int(input())
for test_case in range(1, K+1):
    students = list(map(int, input().split()))
    
    del students[0]
    A = sorted(students, reverse = True)

    max_ = 0

    for i in range(1, len(A)):
        if A[i-1] - A[i] > max_:
            max_ = A[i-1] - A[i]
    
    print(f"Class {test_case}")
    print('Max {}, Min {}, Largest gap {}'.format(max(A), min(A), max_))