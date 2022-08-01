color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
color_input = []
for a in range(3):
    color_input.append(input())
result = int(str(color.index(color_input[0])) + str(color.index(color_input[1]))) * (10**(color.index(color_input[2])))
print(result)