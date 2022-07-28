N =int(input())
number = {}
number_list = []

for a in range(N) :
    T = int(input())
    number[T] = number.get(T, 0) +1

new_number = sorted(number.keys())
for a in new_number :
    if number[a] == max(number.values()):
        print(a)
        break

    









