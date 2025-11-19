# revering array

arr=[2,3,4,4,5,6,7,10,11,100]
l=0
r=len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1

print(arr)


# find max and min values in raange

a2=[34,42,45,62,67,73,27,88,33,58]
a2.sort(reverse=True)
print(a2[0])