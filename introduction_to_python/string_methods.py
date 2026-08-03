'''
Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling(opens in a new tab). 
Remember, \n is a special sequence of characters that causes a line break (a new line).

'''

'''
Use the code editor below to answer the following questions about verse and use Test Run to check your output in the quiz at the bottom of this page.

1- What is the length of the string variable verse?
2- What is the index of the first occurrence of the word 'and' in verse?
3- What is the index of the last occurrence of the word 'you' in verse?
4- What is the count of occurrences of the word 'you' in the verse?

You will need to refer to Python's string methods documentation(https://docs.python.org/2/library/string.html).
'''
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

# Length of the string variable verse
length_of_verse = len(verse)


# The index of the first occurrence of the word 'and' in verse
first_index = verse.find("and")

# The index of the last occurrence of the word 'you' in verse
last_index = verse.rfind("you")

# The count of occurrences of the word 'you' in the verse
occurences_of_you = verse.count("you")

print(verse)
