# shallow copy and deep copy
import copy
# shallow copy --- (.copy() method use)
l1=[1,2,3,[23,4,5,6],[645,863,4973]]
l2=copy.deepcopy(l1)
l2[3][1]=500
print(l1,l2)


