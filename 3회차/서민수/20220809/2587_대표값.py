# 숫자를 받아줄 빈 리스트
a = []
for _ in range(5):
    score = int(input())
    # score에 정수들을 a에 추가
    a.append(score)
# 평균 구하기
avg = sum(a) // 5
# 정렬후 가운데 인덱싱
cen = sorted(a)[2]
print(avg)
print(cen)
