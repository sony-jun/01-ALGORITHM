a=0
for i in range(8):
     a+=input()[i%2::2].count('F')
print(a)