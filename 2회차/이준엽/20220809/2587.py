n_sum = 0
numbers = []
for i in range(5):
    number = int(input())
    n_sum+=number
    numbers.append(number)
numbers.sort()
print(round(n_sum/5),numbers[2],sep='\n')