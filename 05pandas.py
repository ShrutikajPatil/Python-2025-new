import pandas as pd

# sample data
df = pd.DataFrame({"value":[1,1,1,3,2,4,2,3]})
print(df)

# step 1: count frequency
freq = df['value'].value_counts()
print(freq)

# # step 2: get second most repeated element
second_high = freq.index[1]

print("Second highly repeated element:", second_high)