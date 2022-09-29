import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u'] #모음 리스트 만들기

while True: 
    stc = list(input().lower())  #소문자 형태로 문장 input 받음
    cnt = 0  #모음의 개수

    if stc[0] == '#':   #첫번째 인덱스에 #있으면 종료
        break

    for i in stc: 
        if i in vowels:  #변수 i가 모음리스트에 있으면
            cnt += 1
    
    print(cnt)
    

# for i in range(3):
#     stc = list(input().lower())
#     cnt = 0

#     for j in stc:
#         if j in vowels:
#             cnt += 1
#     if stc[0] == '#':
#         break   
#     print(cnt)