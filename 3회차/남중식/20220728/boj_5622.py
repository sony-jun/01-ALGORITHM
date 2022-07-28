num_dict = {2 : ['A', 'B', 'C'],
            3 : ['D', 'E', 'F'],
            4 : ['G', 'H', 'I'],
            5 : ['J', 'K', 'L'],
            6 : ['M', 'N', 'O'],
            7 : ['P','Q','R','S'],
            8 : ['T','U','V'],
            9 : ['W','X','Y','Z']
            }

T = input()

sum = 0
for t in T:
    for k, v in num_dict.items():
        if t in v:
            sum = sum + k + 1
print(sum)