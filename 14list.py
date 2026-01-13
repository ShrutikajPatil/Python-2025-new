chai=['Masala','Mint','Ginger','Oolong','Black','green']
# print(chai)
# print(chai[0])
# print(chai[5])
# print(len(chai))
# print(chai[len(chai)-1])

# chai[1]='Herbal'
# print(chai)

# chai[1:2]='Lemon'   //adding all indivual elements like 'L','e','m','o'
# chai[1:2]=['Lemon']
# print(chai)


# print(chai[1:1]) # empty [] return

# chai[1:1]=[]  //
# print(chai)



# for i in chai:
#     print(i,end=' Tea,')

# if 'Masala' in chai:
#     print("yes I have")

# else:
#     print("I dont have")   



# chai.pop()
# print(chai)    

# chai.remove('Black')
# print(chai)


# chai.append('Black')
# chai.insert(1,'White')
# print(chai)


chai_copy=chai.copy()

chai_copy.append("Pink")
print(chai)
print(chai_copy)




nums=[i*6 for i in range(1,11)]
print(nums)