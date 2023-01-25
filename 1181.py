import sys
input=sys.stdin.readline
arr=[]
leng=[]
a=int(input())
for i in range(a):
    arr.append(input())

for i in set(arr):
    leng.append((len(i),i))
ans=sorted(set(arr))
for len_word, word_list in ans:
    print(word_list)