charList=['c=','c-','dz=','d-','lj','nj','s=','z=']
replaceList=['C','c','D','d','L','N','S','Z']

char = input()
for i in range(len(char)*2):
    try:
        char = char.replace(charList[i],replaceList[i])
    except:
        pass
print(char)
print(len(char))