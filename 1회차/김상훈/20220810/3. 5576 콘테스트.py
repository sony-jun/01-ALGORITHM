import sys
sys.stdin = open("3. 콘테스트.txt", "r")

N = 20 #참가자 20명
w_c = [] # 참가자 점수 넣을 리스트 => 나중에 w 대학 참가자 인원의 점수만 저장할 예정.
k_c = [] # k대학 참가자들 점수 넣을 리스트.
for _ in range(N):
    score = int(input())
    w_c.append(score)
k_c = w_c[10:] # 11번째부터 끝까지 슬라이싱해서 k_c에 넣어준다.
w_c = w_c[:10] # 10번째 자리까지 잘라서 리스트를 재정의함.

w_c.sort(reverse=True)
k_c.sort(reverse=True) # 각 대학 점수 내림차순 정렬(큰 수가 맨앞)

print(sum(w_c[0:3]),end=' ') # 앞에서부터 3번째 자리까지 출력
print(sum(k_c[0:3]))
