import sys
sys.stdin = open('B5800.txt')

K = int(input())
for k in range(1, K+1):
    scores = list(map(int, input().split()))
    students = scores.pop(0)
    scores.sort(reverse=True)
    gaps = []
    # print(students, scores)   
    for i in range(students-1): # 두개씩 차이를 계산하니까. 젤 마지막꺼 인덱스 벗어나는거 방지
        gaps.append(scores[i] - scores[i+1])     
  
    print(f'Class {k}')
    print('Max ', max(scores), ', Min ', min(scores), ', Largest gap ', max(gaps), sep='')