import sys

sys.stdin = open("5. 성적 통계.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    
    c = list(map(int,input().split())) # [5 30 25 76 23 78]
    max_gap = 0 #  인접한 점수 차이가 가장 큰 것을 넣을 공간
    student_number = c[0] 
    c = c[1:] # 맨 앞에 학생 수인 c[0]를 빼고 c[1]부터 저장.
    c.sort(reverse=True) # [78 76 30 25 23] #내림차순 정렬
    
    for i in range(student_number-1): # 맨 뒤 요소(23)는 뺄 것이 없으므로 길이에서 -1을 범위로 지정.
        m_gap = (c[i]-c[i+1]) # c[0]-c[1] ~~ c[3]-c[4] 각 빼기값을 m_gap에 저장
        if m_gap > max_gap: # m_gap이 max_gap보다 크면 
            max_gap = m_gap # max_gap에 해당 값을 넣어줌. 
            
    print(f'Class {t}')        
    print(f'Max {max(c)}, Min {min(c)}, 'f'Largest gap {max_gap}')