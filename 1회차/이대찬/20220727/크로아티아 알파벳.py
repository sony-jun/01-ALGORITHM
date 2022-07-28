lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str_ = input()
result =0
for i in lst:
    cnt = 0;
    tmp = ''
    tmp = str_.replace(i,'*')
   
    for i in tmp:
        if i == '*':
            cnt +=1
            result += cnt 
   
    str_ = tmp.replace('*',' ')

str_ = str_.replace(' ','')  

result += len(str_)

print(result)



 