t = int(input())
i=0
while i < t:
    st = str(input())
    length = len(st)
    j = 0
    cnt = 0
    while j < length:
        
        num = int(st[j])
        #print(num)
        if num == 4:
            cnt = cnt + 1
        j=j+1
    print(cnt)
    i=i+1