dic = {('A','B','C') : 2, ('D','E','F') : 3, ('G','H','I') : 4,
       ('J','K','L') : 5, ('M','N','O') : 6, ('P','Q','R','S') : 7,
       ('T','U','V') : 8, ('W','X','Y','Z') : 9}

str_ = input()

result = 0

for str in str_:
    for k in dic:
        if str in k:
            result += dic[k]+1

print(result)            
        

 