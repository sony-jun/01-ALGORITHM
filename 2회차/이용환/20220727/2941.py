text_= input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=','z=']
for i in cro :
    if i in text_ :
        text_ = text_.replace(i,'a')
print(len(text_))