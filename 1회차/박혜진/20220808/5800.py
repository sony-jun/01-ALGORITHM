# 각 반 학생들의 최대, 최소, 점수 차이

for i in range(int(input())) :
    math = list(map(int, input().split()))
    math = sorted(math, reverse=True)

    print(math)
    # print(f'Class {i+1}')
    
    # gap = []
    # for j in len(math) :        
        
    #     while math[j+1] != min(math) :
    #         gap.append(math[j] - math[j+1])

    #     if math[j+1] == min(math) :
    #         gap.append(math[j] - math[j+1])

    # print(f'Max {max(math)}, Min {min(math)}, Largest gap {max(gap)}')