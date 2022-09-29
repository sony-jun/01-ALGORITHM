# 2941번 크로아티아 알파벳

sen = input() 
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 

for i in croatia: 
    while(True): 
        if i in sen: 
            start = sen.find(i) 
            sen = sen.replace(sen[start: start+len(i)], 'q') 
        else: 
            break 

print(len(sen))