enchar =[
     'ABC',
     'DEF',
     'GHI',
     'JKL',
     'MNO',
     'PQRS',
     'TUV',
     'WXYZ'
]
a = input().upper()
result = 0

for char_list in enchar:
    

    for char_list_list in char_list:
        for input_list in a:
            
            if char_list_list == input_list:
                result += enchar.index(char_list) + 3
print(result)