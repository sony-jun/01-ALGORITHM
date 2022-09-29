word = "23four5six7"
 
re_dict = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6', 'seven': '7', 
    'eight': '8', 'nine': '9'
}
for key, value in re_dict.items():
    word = word.replace(key,value)

print(int(word))