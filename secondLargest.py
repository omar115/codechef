r=[]
s=[]
t = int(input())
for _ in range(t):
    s = list(map(int,input().split()))
    r.append(s)

for _ in range(t):
    r[_].sort(reverse=True)
    print(r[_][1])