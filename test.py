# def divisible_by_five(n):
#     if(n % 5 == 0):
# 	    return True
#     else:
#         return False

# print(divisible_by_five(21))


# #less than 100
# def less_than_100(a, b):
#     if(a + b < 100):
#         return True
#     else:
#         return False


# print(less_than_100(90, 9)

# def frames(minutes, fps):
#     	return (minutes * 60) * (fps)
#         #return results
        
# print(frames(60,1))

# def divisible(num):
#     if(num % 100 ==0):
#         return True
#     else:
#         return False
# print(divisible(100))

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

