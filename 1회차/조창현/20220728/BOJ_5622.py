#word = 'WA'
word = input()

num_dict = {
    'ABC' : 3,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXZY' : 10
}
time = 0

for i in word:
    #print(i)
    for j in num_dict:
        #print(j)
        if i in j:
            #print(j)
            time += num_dict.get(j)
print(time)