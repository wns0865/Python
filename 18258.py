import sys
from collections import deque
import sys
input=sys.stdin.readline

def empty() :
    if(len(arr))==0:
        return 1
    else: return 0
def push(x) :
    arr.append(x)
def pop():
    if empty()==1:
        print("-1")
    else:print(arr.popleft())
def size():
    print(len(arr))
def front():
    if empty() == 1:
        print("-1")
    else:print(arr[0])
def back():
    if empty() == 1:
        print("-1")
    else:print(arr[len(arr)-1])

arr = deque([])
n=int(input())
for i in range(n):
    rq=input().split()
    if rq[0]=="push":
        push(rq[1])
    elif rq[0]=="pop":
        pop()
    elif rq[0] =="size":
        size()
    elif rq[0] =="empty":
        print(empty())
    elif rq[0] =="front":
        front()
    elif rq[0] =="back":
        back()