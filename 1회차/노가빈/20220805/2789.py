delStr = list('CAMBRIDGE')
str = input()
for chr in delStr:
    str = str.replace(chr,'')
print(str)