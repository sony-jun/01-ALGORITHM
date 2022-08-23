absolutes = [4, 7, 12]
signs = [True, False, True]

real_num = []

for i in range(len(absolutes)):
    if signs[i] == True:
        real_num.append(absolutes[i])
    else:
        real_num.append(-absolutes[i])

print(sum(real_num))