

# 🟢 BASIC PYTHON CODING QUESTIONS (10)

# Write a program to swap two numbers without using a third variable.

a=10
b=20
a=a+b  
b=a-b  
a=a-b

print(a,b)


# Write a function to check if a number is even or odd.

def isEvenOdd(n):
    if n%2==0:
        return 'EVEN NUMBER'
    else:
        return 'ODD'




n=19
print(isEvenOdd(n))

# Write a program to find the factorial of a number.

def fact(n):
    l=n
    f=1
    while(n>0):
        f=f*n
        n-=1
    return f'factorial of {l} is {f}'    

n=4
print(fact(n))

# Write a program to reverse a string.
def revStr(s):
    # return s[::-1]
    l=len(s)-1
    n=""
    while(l>=0):
        n=n+s[l]
        l-=1
    return n
s='Patil shrutika'
print(revStr(s))

# Write a program to find the largest number in a list.

def largestEl(arr):
    max=arr[0]
    for i in arr:
        if i>max:
            max=i

    print('largest element in list is',max)        

arr=[3,4,5,1]
largestEl(arr)

# Write a program to count vowels in a string.

def vowel_count(str):
    count=0
    vowel=['a','i','o','u','e']
    for i in str:
        if i in vowel:
            count+=1

    return count        


str='shrutika patil'
print(vowel_count(str))

# Write a program to check if a string is a palindrome.

def isPalindrom(s):
    s=s.lower()
    new=""
    l=len(s)-1

    while(l>=0):
        new=new+s[l]
        l-=1

    return s==new    


s='Madam'
print(isPalindrom(s))

# Write a program to remove duplicates from a list.

def remove_dup(arr):
    new=[]
    for i in arr:
        if i not in new:
            new.append(i)

    return new        

arr=[3,4,5,4,5]
print(remove_dup(arr))

# Write a program to find the sum of all elements in a list.

def sum_all_el(arr):
    count=0

    for i in arr:
        count=count+i
    return count 


arr=[3,4,5,4,5]
print(sum_all_el(arr))



# Write a program to count the frequency of characters in a string.
def count_freq(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d        
             

s='ssbbccdddcca'
result=count_freq(s)
print(result)




# 🟡 MEDIUM PYTHON CODING QUESTIONS (10)
# Write a program to find the second largest element in a list.
def second_large(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    
    return f'second largest elemet is ',arr[1]
arr=[3,4,5,1]
print(second_large(arr))

# Write a program to check if two strings are anagrams.

def check_anagram(s1,s2):
    s1=sorted(s1)
    s2=sorted(s1)
    return s1 == s2
s1='see'
s2='ees'
print(check_anagram(s1,s2))



# Write a program to find duplicate elements in a list.
def find_dup(arr):
    unique=[]
    dup=[]
    

    for i in arr:
        if i not in unique:
            unique.append(i)
        else:
            dup.append(i)

    return dup        


print(find_dup([1,2,2,3,4,5,1]))

# Write a program to flatten a nested list.
def flatten(arr):
    new=[]
    for i in arr:
        if isinstance(i,list):
            new.extend(flatten(i))
        else:
            new.append(i)


    return new            



arr=[1,2,[3,4,[5]],7]
print(flatten(arr))


# Write a program to find the intersection of two lists.

def intersect(arr,arr2):


    # res=list(set(arr) & set(arr2))
    # print(res)
    res=[]
  
    for i in arr:
        if i in arr2:
            res.append(i)

    print(res)



arr=[1,2,3,4]
arr2=[2,3,5,6]
intersect(arr,arr2)

# Write a program to count word frequency in a sentence.
def freq_count(s):
    fre={}
    s=s.split(' ')
    for i in s:
        if i not in fre:
            fre[i]=1
        else:
            fre[i]+=1

    return fre            




s='hello shrutika How are you, hello shrutika'
print(freq_count(s))


# Write a program to sort a dictionary by values.

def sort_dict(d):
   new_d=dict(sorted(d.items(),key=lambda item:item[1]))

   print(new_d)

d={'a':2,'b':1,'c':3,'d':4}
sort_dict(d)

# Write a program to find all prime numbers in a given range.

            





# Write a program to rotate a list by k positions.

# Write a program to check if a number is Armstrong number.