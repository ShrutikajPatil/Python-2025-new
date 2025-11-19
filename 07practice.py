                
def secondHigh(lst):
    d={}
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1    

    print(d)

    sorted_d=list(d.items())
    print(sorted_d)

    for i in range(len(sorted_d)):
        for j in range(i+1,len(sorted_d)):
            if sorted_d[i][1] < sorted_d[j][1]:
                sorted_d[i],sorted_d[j]=sorted_d[j],sorted_d[i]
    

    print(sorted_d[1][0])

I=[1,1,1,3,2,4,2,3]
secondHigh(I)





arr=[1,1,1,3,2,4,2,3]

map_d={}

for i in arr:
    if i not in map_d:
        map_d[i]=1
    else:
        map_d[i]+=1    


