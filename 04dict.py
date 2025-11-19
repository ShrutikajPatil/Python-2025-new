lst=[1,1,1,3,2,4,2,3]
def second_highly_repeated(lst):
    # Step 1: Count frequency of each number
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Sort by frequency in descending order
    sorted_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)

    # Step 3: Return the second highly repeated element
    print(sorted_freq)
    return sorted_freq[1][0]

i = [1,1,1,3,2,4,2,3]
print(second_highly_repeated(i))