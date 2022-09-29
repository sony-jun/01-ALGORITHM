book_count = int(input())
dic_sell = {}

for i in range(book_count):
    book = input()
    dic_sell.setdefault(book,0)
    dic_sell[book] += 1
# max가 둘이면 사전순으로 앞에 오는거

maxlist = [k for k,v in dic_sell.items() if max(dic_sell.values())==v]
# maxlist = []
# for k,v in dic_sell.items():
#     if max(dic_sell.values())==v:
#         maxlist.append(k)
maxlist.sort()
print(maxlist[0])