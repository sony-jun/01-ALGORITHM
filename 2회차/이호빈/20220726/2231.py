number = int(input())
parted = []

# n = 12345
# n_list = list(map(int, str(n))
# [1, 2, 3, 4, 5]


for num in range(1, number + 1): 
    digit_ = list(map(int, str(num))) #sum은 리스트에서만 사용 가능,
    result = num + sum(digit_)
    if  number == result:
        print(num)
        break
else:
    print(0)    

