absolutes = [4,7,12]
sum = 0
signs = input()
signs = signs.lstrip('[').rstrip(']').split(',')
for i in range(len(absolutes)):
    if signs[i] == 'false':
        sum -= absolutes[i]
    elif signs[i] == 'true':
        sum += absolutes[i]
print(sum)

