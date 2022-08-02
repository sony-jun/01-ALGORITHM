# input is a serial of alphabets. input can be both upper and lower cases
# find most used alphabet and printout in caps
# if output is equal or more than 2 then print out '?'
# output must bbe in caps!!!
#   change output as a number via ASCII code using 'ord' method. 
#   If the output is higher than 96 then deduct 32
#   use 'chr' method on number to change back to alphabet

word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])