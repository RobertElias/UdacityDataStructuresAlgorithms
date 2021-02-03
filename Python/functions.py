# Example function 1: return the sum of two numbers.
def sum(a, b):
    return a+b

# Example function 2: return the size of list, and modify the list to now be sorted.

my_list = ["Robert", "Cynthia", "Robbie"]
def list_sort(my_list):
    my_list.sort()
    return len(my_list),  my_list
print(list_sort(my_list))


################################################
# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2


my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))
###############

#fibonacci


def prod(a, b):
    # TODO change output to the product of a and b
    return a*b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120

### sudoku test

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

# Define a function check_sudoku() here:
def test_sudoku(square):
    for row in square:


        check_list = list(range(1, len(square[0])+ 1))
        for i in row:
            if i not in check_list:
                return False
                check_list.remove(i)
    
    for n in range(len(square[0])):

        check_list = list(range(1, len(square[0])+1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True


print(test_sudoku(incorrect))
#>>> False

print(test_sudoku(correct))
#>>> True

print(test_sudoku(incorrect2))
#>>> False

print(test_sudoku(incorrect3))
#>>> False

print(test_sudoku(incorrect4))
#>>> False

print(test_sudoku(incorrect5))
#>>> False
