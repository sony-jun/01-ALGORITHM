num2017 = [0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10]
num2018 = [0,512,256,256,128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]
t = int(input())
for i in range(t):
    n1,n2 = map(int,input().split(' '))
    if n1 <= len(num2017) and n2 <= len(num2018):
        print(int(str(num2017[n1] + num2018[n2]) + '0000'))
    elif n1 > len(num2017)and n2 <= len(num2018):
        print(int(str(num2018[n2]) + '0000'))
    elif n1 <= len(num2017)and n2 > len(num2018):
        print(int(str(num2018[n1]) + '0000'))
    else:
        print(0)

