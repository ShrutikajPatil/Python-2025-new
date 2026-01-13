# 1️⃣ Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Input: "abcabcbb"
# Output: 3 
def longest_sub_str(s):
    max_len=0
    longest =''
    for i in range(len(s)):
        visited={}
        temp=""
        for j in range(i,len(s)):
            if s[j] in visited:
                break
            visited[s[j]]=True
            temp=temp+s[j]

        print(temp)
        if len(temp) > max_len:
            max_len=len(temp)
            longest=temp


    print(max_len)
    print(longest)

s= "abcabcbb"
longest_sub_str(s)