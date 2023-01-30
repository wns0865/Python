import sys
input=sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

dict = {} 
for i in range(len(cards)):
    dict[cards[i]] = 0  

for j in range(M):
    if checks[j] not in dict:
        print(0, end=' ')
    else:
        print(1, end=' ')