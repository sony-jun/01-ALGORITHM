import sys
sys.stdin = open("5622.txt")

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', "PQRS", "TUV", "WXYZ"]
abc = list(input()) 
time = 0 # 시간 초기화
for i in range(len(abc)): # 입력받은 단어(abc)의 len만큼 i를 반복적 수행
    for j in dial: # dial에 있는 문자열 하나하나를 j로 반복
        if abc[i] in j: # 입력받은 단어(abc)가 j의 문자열에 해당한다면
            time += dial.index(j) + 3 #dial 리스트에 있는 j의 위치에 3만큼 더한 것을 time에 할당
print(time)

# 다른 풀이
# dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# sec = [3, 4, 5, 6, 7, 8, 9, 10]     # dial : 문자열, sec : 소요시간

# word = input()
# time = 0

# for c in word:                      # 입력받은 문자열의 각 문자 c
#     for i in range(len(dial)):      # 다이얼 처음부터 끝까지 인덱스 i
#         if c in dial[i]:            # c가 해당 다이얼에 속하는지 확인
#             time += sec[i]          # time에 해당 소요시간을 더하기

# print(time)                         # 최종 소요시간 time 출력