
w_school = []
w_sum = 0
k_school = []
k_sum = 0
for i in range(10):
    w_school.append(int(input()))
w_school.sort()
for i in range(3):
    w_sum += w_school[-1]
    w_school.pop()
for i in range(10):
    k_school.append(int(input()))
k_school.sort()
for i in range(3):
    k_sum += k_school[-1]
    k_school.pop()
print(w_sum,k_sum)



