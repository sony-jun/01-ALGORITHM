# 폴문의 레인지의 첫번째 인자는 초기값, 두번째 인자, 종료값으로, 첫번째와 마지막은 생략이다.
# 종료값의 경우 해당 값을 포함하지 않기 떄문에 =1 을 해준다. sem을 통해 for문을 완성해준다.

a = int(input())
sum = 0
for i in range(a+1):
    sum = sum + i
print(sum)