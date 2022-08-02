dic = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
n = input()
str_lst = []
for i in n:
    str_lst.append(i)
    #['o','n','e']
    if ''.join(str_lst) in dic:
        #one
        print(dic[''.join(str_lst)],end = '')
        #1
        str_lst = []
        #초기화 

    elif i.isdigit() == True:
        print(i,end ='')
        str_lst = []
