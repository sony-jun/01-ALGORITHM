k = int(input())            # k = number of classes
student = []

for j in range(1,k+1):
    student = list(map(int,input().split()))
    student = student[1:]
    s_student = sorted(student)
    Highest = max(s_student)
    Lowest = min(s_student)
    Lg = 0
    
    for i in range(0,len(s_student)-1): 
        if s_student[i+1] - s_student[i]>Lg:
            Lg = s_student[i+1] - s_student[i]
    
    print(f'Class {j}')
    print(f'Max {Highest}, Min {Lowest}, Largest gap {Lg}')