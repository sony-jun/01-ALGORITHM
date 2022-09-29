T = int(input())

for tc in range(T):
    list_ = []
    list_ = list(map(int, input().split()))
    gap = []

    list_ = list_[1:]
    list_.sort(reverse=True)
    max_ = list_[0]
    min_ = list_[len(list_)-1]
        
    for i in range(len(list_)-1):
        gap.append(list_[i] - list_[i+1])
    
    max_ = 'Max' + ' ' + str(max_)
    min_ = 'Min' + ' ' + str(min_)
    Largest_gap = 'Lagrest gap' + ' ' + str(max(gap))
    
    print(f'Class {tc+1}')
    print(max_,min_,Largest_gap,sep=', ')