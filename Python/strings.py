# Quiz: Fix the Quote
# The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. First run it with Test Run to view the error message. Then resolve the problem so that the quote(from Henry Ford) is correctly assigned to the variable ford_quote.

ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)


# Quiz: Write a Server Log Message
# In this programming quiz, you’re going to use what you’ve learned about strings to write a logging message for a server.

# You’ll be provided with example data for a user, the time of their visit and the site they accessed. You should use the variables provided and the techniques you’ve learned to print a log message like this one(with the username, url, and timestamp replaced with values from the appropriate variables):

# Yogesh accessed the site http: // petshop.com/pets/reptiles/pythons at 16: 20.

# Use the Test Run button to see your results as you work on coding this piece by piece.


username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site " + url + " at " + timestamp+".")


# Quiz: len()
# Use string concatenation and the len() function to find the length of a certain movie star's actual full name. Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name!


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# todo: calculate how long this name is
name_length = (len(given_name+middle_names+family_name))

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
