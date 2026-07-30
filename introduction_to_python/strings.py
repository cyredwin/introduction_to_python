'''
The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. First run it with Test Run to view the error message. Then resolve the problem so that the quote (from Henry Ford(opens in a new tab)) is correctly assigned to the variable ford_quote.
'''
# Fix this string!
# ford_quote = 'Whether you think you can, or you think you can't--you're right.'
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

'''
We’ve already seen that the type of objects will affect how operators work on them. What will be the output of this code?
'''
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count) 
# Awnser : 3415 ( and tropical_fruit_count is a string )

'''
You’ll be provided with example data for a user, the time of their visit and the site they accessed. You should use the variables provided and the techniques you’ve learned to print a log message like this one (with the username, url, and timestamp replaced with values from the appropriate variables):

Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.
'''
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

#  print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

message = username + " " + "accessed the site" + " " + url +" "+ "at"+" "+ timestamp + "."
print(message)


'''
Use string concatenation and the len() function to find the length of a certain movie star's actual full name. 
Store that length in the name_length variable. 
Don't forget that there are spaces in between the different parts of a name
'''

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + " " + middle_names + " " + family_name)  # calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)