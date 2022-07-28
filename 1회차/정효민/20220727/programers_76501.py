absolutes = [9 , 12 , 2]
true = 0
false = 1
signs = [true , false , true]
result = []

for i in range(len(absolutes)):
    if signs[i] == true:
        absolutes[i] = absolutes[i] * 1
        result.append(absolutes[i])
        #print(absolutes[i] , type[absolutes[i]])
    elif signs[i] == false:
        absolutes[i] = absolutes[i] * -1
        result.append(absolutes[i])   
print(sum(result))
        