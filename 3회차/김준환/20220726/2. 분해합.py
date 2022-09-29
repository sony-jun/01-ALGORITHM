# 숫자 범위는 입력한 숫자 에서 9*len(입력숫자) 뺀 숫자까지
# 1씩 증가시키며 조건 충족하는지 확인
# 조건 충족시키는 값은 리스트에 저장해서 최소값 출력

num = input()
maker_lst = []

for maker in range(1,int(num)):
    num_sum = []
    for i in str(maker):
        num_sum.append(int(i))
    num_sum.append(maker)
    if sum(num_sum) == int(num):
        maker_lst.append(maker)

if sum(maker_lst) == 0:
    maker_lst=[0]
print(min(maker_lst))