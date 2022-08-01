note, dummy = map(int, input().split())

result = True
cnt = note

while cnt > 0:
    note_cnt = int(input())
    note_list = list(map(int, input().split()))
    if note_list != sorted(note_list, reverse = True):
        result = False
    cnt -= note_cnt

if result:
    print('Yes')
else:
    print('No')