# Write a function to flatten nested lists.
# Example:
# Input: [1, [2, [3, 4], 5], 6]
# Output: [1, 2, 3, 4, 5, 6]
# def flatten(arr):
#     flat=[]
#     for i in arr:
#         if isinstance(i,list):
#             flat.extend(flatten(i))
#         else:
#             flat.append(i)    
#     return flat
# Input=[1, [2, [3, 4], 5], 6]

# result=flatten(Input)
# print(result)




# write a function which returns 2nd highly repeated element in the list.
# def secondHigh(l):
#     map_h={}
#     for i in l:
#         if i not in map_h:
#             map_h[i]=1
#         else:
#             map_h[i]+=1

#     print(map_h)  
#     f=list(map_h.items())
#     print(f)
#     for i in range(len(f)):
#         for j  in range(i+1,len(f)):
#             if f[i][1]<f[j][1]:
#                 f[i],f[j]=f[j],f[i]

#     print(f[1][0])                      

# l = [1,1,1,3,2,4,2,3]
# secondHigh(l)



# # reverse a string

# s='shrutika'
# new=''
# # print(s[::-1])
# for i in s:
#     new=i+new
# print(new)    



# # reverse the array

# arr=[300,200,100,600,700,20,500]
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1


# print(arr)    



# min=arr[0]

# for i in arr:
#     if i<min:
#         min=i
# print(min)         

# for i in arr:
#     if i>min:
#         min=i
# print('max el',min) 



# sort the array in ascending order:

# arr=[300,200,100,600,700,20,500]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]>arr[j]:
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp        

# print(arr)
# factorial of number


# def fact(n):
#     f=1
#     while(n>0):
#         f=n*f
#         n-=1

#     print(f) 
  
# n=6

# fact(n)



# # check the number is prime or not
# def is_prime(i):
#     count=0
#     div=2
#     while(i>=div):
#         if i%div==0:
#             count+=1

#         div+=1
#     if count==1:
#         return i
# def checkPrime(n):
#     prime=[]
#     for i in range(2,n+1):
#        if is_prime(i):
#            prime.append(i)    
#     return prime 
# n=11
# print(checkPrime(n))



# Q ....you have given sorted list arr=[3,4,5,7,8,9] and k=6 , you have to insert this k in list as sorted manner
# arr = [3, 4, 5, 7, 8, 9]   #6
# k = 10

# i=0
# while i<len(arr) and arr[i]<k:
#     i+=1
# arr.insert(i,k)
# print(arr)    





# given an integer array nums, move all 0's to the end while 
# maintaing the relative order of the non-zero elemets
# nums=[0,1,0,3,12]
# def fun(nums):
#     non_zero=[]
#     zero=[]
#     for i in nums:
#         if i!=0:
#             non_zero.append(i)
#         else:
#             zero.append(i) 

#     non_zero=sorted(non_zero)
#     print(non_zero)
#     print(zero)
#     print(non_zero+zero)
# nums=[0,1,0,3,12,11]
# fun(nums)


chars = [ch for ch in "shrutika"]
print(chars)
