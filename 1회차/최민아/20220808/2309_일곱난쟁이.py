import sys
sys.stdin = open("20220808/2309_일곱난쟁이.txt")

seven = []                              # 난쟁이들 키 리스트
for i in range(9):                      # 아홉 명
    seven.append(int(input()))          # 리스트에 저장

for i in range(8):
    for j in range(i+1, 9):
        if seven[i] + seven[j] == sum(seven) - 100:   # 가짜 둘의 키 합 = 아홉 명 키 - 100 
            no_1 = seven[i]             # 가짜 난쟁이1
            no_2 = seven[j]             # 가짜 난쟁이2

seven.remove(no_1)                      # 가짜 난쟁이1 키 삭제
seven.remove(no_2)                      # 가짜 난쟁이2 키 삭제

seven.sort()                            # 남은 일곱난쟁이 키 정렬
for i in seven:
    print(i)                            # 순서대로 출력