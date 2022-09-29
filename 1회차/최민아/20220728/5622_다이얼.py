import sys
sys.stdin = open("20220728/5622_다이얼.txt")

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sec = [3, 4, 5, 6, 7, 8, 9, 10] # dial : 문자열, sec : 소요시간

word = input()
time = 0

for c in word:                  # 입력받은 문자열의 각 문자 c
    for i in range(len(dial)):  # 다이얼 처음부터 끝까지
        if c in dial[i]:        # c가 해당 다이얼에 속하는지 확인
            time += sec[i]      # time에 해당 소요시간을 더하기

print(time)                     # 최종 소요시간 time 출력