
def sum_def(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True :
            absolutes[i] = absolutes[i]
        else:
            absolutes[i] = -absolutes[i]

    return sum(absolutes)

print(sum_def([4,7,12]	, [True,False,True]	))