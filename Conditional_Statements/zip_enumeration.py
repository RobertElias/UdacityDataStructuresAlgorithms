letters = ['a','b','c']
nums = [1,2,3]
#zip function
for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))


print("------------------------------------")

#Enumerate function
for i, letter in enumerate(letters):
    print(i, letter)