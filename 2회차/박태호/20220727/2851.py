# 처음부터 더해 나가고 
# if 지금 값이 - 100 의 절대값이 
#    다음 값 - 100 의 절대값 둘 중 수가 적은 놈을 출력
#시작은 for 입력 sum_함수에 더해나감
sc_li = []
sum_ = 0
result = []
for i in range(10):
    sc = int(input())
    sum_ = sum_ + sc
    sc_li.append(sum_)

for i in range(len(sc_li)):
    result.append(abs(sc_li[i]-100))


if result.count(min(result)) > 1 : #값이 2개면..
    print(sc_li[result.index(min(result))+1]) # 다음 인덱스 값
    # [ 80 ,120] 중 120을 출력한다는 말
else:
    print(sc_li[result.index(min(result))])
    
