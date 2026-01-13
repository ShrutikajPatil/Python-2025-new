arr=[1,1,2,2,2,3,4,5,6,9,10,10,10]
map_d={}
for i in arr:
    if i not in map_d:
        map_d[i]=0

print(map_d)        

j=0
for k in map_d:
    arr[j]=k
    j+=1

print(j)    


def reverse(a):
    left=0
    right=len(a)-1
    while left<right:
        a[left],a[right]=a[right],a[left]
        left+=1
        right-=1

    print(a)    




a=[3,4,6,56,45,100]
reverse(a)
# n=len(a)

# temp=a[n-1]
# for i in range(n-2,-1,-1):
#     a[i+1]=a[i]

# a[0]= temp
# print(a)   



a1=[1,2,0,3,4,1,0,0,5,6]
l=len(a1)

temp=[]
for i in a1:
    if i!=0:
        temp.append(i)

print(temp)
t=len(temp)
for j in range(0,t):
    a1[j]=temp[j]

for i in range(t,l):
    a1[i]=0    


print(a1)
# for j in range(l-t):
#     temp.append(0)

# print(temp)



a1=[1,2,0,3,4,1,0,0,5,6]

f={}
for i in a1:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1
print(f)   

list_f=list(f.items())
print(list_f)

for i in range(len(list_f)):
    for j in range(i+1,len(list_f)):
        if list_f[i][1]<list_f[j][1]:
            list_f[i],list_f[j]=list_f[j],list_f[i]


print(list_f)
print(list_f[1][0])    





def isflatten(arr):
    flat=[]

    for i in arr:
        if isinstance(i,list):
            flat.extend(isflatten(i))
        else:
            flat.append(i)


    for i in range(len(flat)):
        for j in range(i+1,len(flat)):
            if flat[i]<flat[j]:
                flat[i],flat[j]=flat[j],flat[i]


    return flat            

arr=[1,2,[4,3,5,10],7,8,[9],6]
print(isflatten(arr))