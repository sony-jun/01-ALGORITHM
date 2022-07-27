m_list = []

for i in range(10):
    m_list.append(int(input()))

sum = 0

for i in range(10):
    diff_100_now = abs(100 - sum)
    diff_100_new = abs(100 - sum - m_list[i])
    
    if diff_100_new <= diff_100_now:
        sum = sum + m_list[i]
    else:
        print(sum)
        break
else:
    print(sum)