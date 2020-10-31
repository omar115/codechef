t = int(input())

for i in range(t):
    
    for j in range(t):
        
        li = []
        
        li.extend([input(),input(),input()])
        
        li.sort()
            
        print(li[-2])
