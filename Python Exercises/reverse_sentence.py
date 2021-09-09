print ('\n============= Sentence Reverser =============')

# get user input
sentence = input ("\nPlease type a multi-word, space-separated sentence:\n")

# split the sentence into a list 
# using the space as a the delimiting character (tokenize)
sentence = sentence.split()

# get the length of the sentence list
number_of_words = len (sentence)

print ('\nnumber_of_words =', number_of_words)



# ------------------------------------------------------------


print ("\n\n\t--- FORWARD ORDER ---")

# counting for loop with reverse indexing
print ('\n- counting for loop -')
for i in range (number_of_words):
    print ( '[', i, ']', sentence [i], sep='', end='  ' )


# automatic for loop
print ('\n\n- automatic for loop -')
for word in sentence:
    print (word, end=' ')



# and more...


# --------------------------------------------------------------

print ('\n\n\n\t--- REVERSE ORDER ---')

# reverse indexing
print ('\n- counting for-loop w/ reverse indexing -')
for i in range (1, number_of_words + 1):
    print ( '[', -i, ']', sentence [-i], sep='', end='  ' )


# keyword 'reversed'
print ('\n\n- keyword \'reversed\' counting for loop -' )
for i in reversed (range (number_of_words)):
    print ( '[', i, ']', sentence [i], sep='', end='  ' )


# advanced range
print ('\n\n- advanced range arguments -')
for i in range (number_of_words - 1, -1, -1):
    print ( '[', i, ']', sentence [i], sep='', end='  ' )



# and more...