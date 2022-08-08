# 영화감독 숌 

N = int(input())

number_ = 666
number_list = []
while True:
    cnt = 0
    str_number = str(number_)
    if '666' in str_number:
        number_list.append(number_)
        number_ += 1
    else:
        number_ += 1

    if len(number_list) == N:
        break
print(number_list[N - 1])
