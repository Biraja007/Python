# Dictionary is a set of key-value pairs refered by a sungle name.
# How to create a Dictionary:
# Syntax: DictionaryName = {"KeyOne":"ValueOne" , "KeyTwo":"ValueTwo"}
ColorOfFruits = {"Apple":"Red" , "Mango":"Yellow" , "Cherry":"Pink"}
print (ColorOfFruits)
print ()

# Values can be retrieved by specifying the key associated with it.
print (ColorOfFruits ["Mango"])
print ()

# A value can be updated by using the key corresponding to that value.
# Syntax: DictionaryName ["Key"] = "NewValue"
ColorOfFruits ["Apple"] = "Green"
print (ColorOfFruits)
print ()

# keys() is used to list all keys in the Dictionary.
# Syntax: DictionaryName.keys ()
print ( ColorOfFruits.keys() )
print ()

# values() is used to list all values present in the Dictionary.
# Syntax: DictionaryName.values ()
print ( ColorOfFruits.values() )
print ()

# del keyword is used to delete a key-value pair.
# Syntax: del DictionaryName  ["Key"]
del ColorOfFruits ["Apple"]
print (ColorOfFruits)
print ()

# copy() is used to copy a contents of one dictionary to another dictionary.
# Syntax: DictionaryTwo = DictionaryOne.copy ()
ColorCopy = ColorOfFruits.copy ()
print (ColorCopy)
print ()

# clear() is used to clear the contents of a dictionary and make it empty.
# Syntax: DictionaryName.clear ()
ColorCopy.clear ()
print (ColorCopy)
