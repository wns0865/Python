import sys
from collections import deque
input=sys.stdin.readline
L=deque([])
n=int(input())

for i in range(n):
    L.append(i+1)
while (len(L)>1):
    L.popleft()
    tmp = L.popleft()
    L.append(tmp)


print(L[0])