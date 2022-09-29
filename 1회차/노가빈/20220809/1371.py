lst = []
while True:
    str = input()
    if str == "":
        print('y')
    try:lst.append(str)
    except:break     
lst = '\n'.join(lst)
print(lst)
