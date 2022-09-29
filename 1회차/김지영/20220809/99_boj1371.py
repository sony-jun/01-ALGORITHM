text = ''
dic_a = {}
while True:
    try:
        text += input().replace(' ', '')
    except EOFError:
        break

for a in text: # a read string
    if a not in dic_a:
        dic_a[a] = 1
    else : dic_a[a] += 1
maxvalue = max(dic_a.values())
maxkey = [k for k,v in dic_a.items() if v == maxvalue]
maxkey.sort()
maxkey = ''.join(maxkey)
print(maxkey)