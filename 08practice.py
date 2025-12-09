# Write a Python function to reverse the string:

# Input: "shrutika"
# Output: "akitruhs"


def reverseStr(s):
    return s[::-1]
s="shrutika"   
print(reverseStr(s) )




# Given a list: arr = [2, 3, 2, 5, 3, 2, 8]
# Count how many times each number appears.

arr = [2, 3, 2, 5, 3, 2, 8]
f_map={}

for i in arr:
    if i not in f_map:
        f_map[i]=1
    else:
        f_map[i]+=1


print(f_map)       



# 3. Find the second largest number in an array (Medium)
# Input: [10, 4, 3, 50, 23, 90]
# Output: 50
# Solve without using built-in functions like sorted().

a= [10, 4, 3, 50, 23, 90]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp



print(a[-2])            



# 4. Check if two strings are anagrams (Medium)
# Two strings are anagrams if they contain same characters in different order.
# Input: "listen", "silent"
# Output: True

s1="listen"
s2="silent"
if len(s1)!=len(s2):
    print(False)

sorted_s1=sorted(s1)  
print(sorted_s1)  
sorted_s2=sorted(s2)
print(sorted_s2)


if sorted_s1==sorted_s2:
    print(True)
else:
    print(False)    




# 5. Move all zeros to the end (Medium).Maintain order of non-zero elements.

# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]



arr = [0, 1, 0, 3, 12,4]

index=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[index],arr[i]=arr[i],arr[index]
        index+=1

print(arr)

print(index)
for i in range(index):
    for j in range(i+1,index):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)



# 1️⃣ Remove duplicates from a list but keep the order (Easy)
# Given a list:

arr = [3, 5, 3, 7, 5, 8]
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)


# 2️⃣ Count uppercase, lowercase, digits, and special characters in a string (Easy)
s="Hello123@World!"
upper_count=0
lower_count=0
digit_count=0
special_char_count=0
for i in s:
    if 'A' <= i <='Z':
        upper_count+=1
    elif 'a' <= i <= 'z':
        lower_count+=1
    elif '1' <= i <='9':
        digit_count+=1

    else:
        special_char_count+=1


print('upper count',upper_count, 'lower count', lower_count, 'digit_count' , digit_count, 'special char count', special_char_count)                    




# 3️⃣ Find all pairs in an array whose sum equals a target (Medium)
# Given:


def target_sum(a,target):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==target:
                print(a[i],a[j])


  
arr = [2, 4, 3, 5, 7, -1, 0, 1]
target = 6

target_sum(arr,target)  


# ✅ 4️⃣ Check if a string contains all unique characters (Medium)
# Write a program to check whether a string contains all unique characters
# (without using set).
# Input: "abcdefa"
# Output: "Not Unique"

def isunique(s):
    s=list(s)
    print(s)

    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                return 'Not Unique'

        return "Unique"    
             
    

   
s='python'
result=isunique(s)
print(result)

# 5️⃣ Find the longest word in a sentence (Easy–Medium)
def longest_word(s):
    s=s.split(' ')
    print(s)
    longest=s[0]
    for i in range(len(s)):
        if len(s[i]) > len(longest):
            longest=s[i]
    print(longest)

sentence = "Python programming is very powerful"
longest_word(sentence)
