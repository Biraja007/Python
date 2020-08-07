# String is a sequence of characters that are enclosed in single or double quotes.
# Syntax: StringName = 'String'
FruitName = 'Mango Is King Of Fruits'
print (FruitName)
print()

# String operations:
# Upper: Converts all characters to uppercase.
# Synatx: StringName.upper()
print ( FruitName.upper() )
print ()

# Lower: Converts all characters to lowercase.
# Synatx: StringName.lower()
print ( FruitName.lower() )
print ()

# Replace: Used to replace a sequence with updated sequence.
# Syntax: StringName.replace ('Old sequence' , 'New sequence')
print ( FruitName.replace ('King' , 'Best') )
print ()

#  Slicing: Returns a slice of string based on index passed.
# Syntax: StringName [StartingIndex : EndingIndex]
print ( FruitName [0:11] )
print ()
# If nothing is mentioned the whole string is printed.
print ( FruitName [:] )
print ()
# Similarly if starting index is not mentioned, characters starting from 0 will be printed.
print ( FruitName [:15] )
print ()
# Similarly if endind index is not mentioned, characters from starting index to end will be printed.
print ( FruitName [13:] )
print ()

# len () returns the length of a string.
print ( len (FruitName) )
print ()

# String formatting in Python is used if one need one string in betwwen of another.
print ('According to me: {}'.format(FruitName) )
print()

# To print a string in reverse.
print(FruitName[::-1])
