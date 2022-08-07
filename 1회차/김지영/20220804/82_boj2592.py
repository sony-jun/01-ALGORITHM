from collections import Counter
num = []
for _ in range(10):
    number = int(input())
    num.append(number)
print(int(sum(num)/len(num))) # 평균
cnt = Counter(num) # 딕셔너리형태로 리스트 빈도값을 구해주는 모듈
print(cnt.most_common(1)[0][0]) # 최빈값