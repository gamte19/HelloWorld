doors =[0] * 101
for i in range(1,101):
    for j in range(1,101):
        if j % i ==0:
            if doors[j] == 0:
        		doors[j] = 1
            else:
        		doors[j] = 0
            j+=1
        else:
            j+=1
    i+=1

for y in range(1,101):
    if doors[y]==1:
        print(y)
