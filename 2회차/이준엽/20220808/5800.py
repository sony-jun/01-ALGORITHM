k = int(input()) 
for i in range(1,k+1):
    numbers = list(map(int,input().split()))
    n = numbers[0]
    scores = numbers[1:]
    m_scores = max(scores)
    min_scores = min(scores)
    scores.sort(reverse=True)
    max_gap = 0
    for j in range(n-1):
        gap = scores[j]-scores[j+1]
        if max_gap<gap:
            max_gap=gap
    print(f'Class {i}\nMax {m_scores}, Min {min_scores}, Largest gap {max_gap}')
