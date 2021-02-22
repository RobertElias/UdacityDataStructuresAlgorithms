# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:

    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)


#using a for loop
# for num in range(2, number + 1):
#     product *= num

#Count By

start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by
print(break_num)#101

#Count By Check

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like you start alue is great then the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    
    result = break_num
print(result)


#nearest square
limit = 40

num = 0

while (num+1)**2 < limit:
    num +=1
nearest_square = num**2

print(nearest_square)
    