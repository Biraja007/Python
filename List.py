# A list is a container that holds many objects under a single name.
#Syntax : ListName = [object1 , object2 , object3]
BestFriends = ['Amit' , 'Biraja' , 'Zoya' , 'Rohit' , 'Mary']
print (BestFriends)

# Values can be accessed by specifying the index value.
BestFriends [2]
print()
# Below are some operations on List:

# Insert: It is used to add a new element at specified index and shift other elements to right.
# Syntax: List.insert (index , element)
BestFriends.insert (1 , 'Ben')
print (BestFriends)
print()

# Remove: It is used to remove an element from the list.
# Syntax: List.remove (element)
BestFriends.remove ('Mary')
print (BestFriends)
print()

# Append: It is used to add a new element at end of the list.
# Syntax: List.append (element)
BestFriends.append ('Johny')
print (BestFriends)
print()

# Sort: It is used to sort the list in ascendind order.
# Syntax: List.sort ()
BestFriends.sort ()
print (BestFriends)
print()

# Reverse: It is used to reverse a list.
# Syntax: List.reverse ()
BestFriends.reverse ()
print (BestFriends)
print()

# Pop: It is used to return an element at specified index and remove it from the list.
# Syntax: List.pop (index)
ReturnValue = BestFriends.pop (3)
print ('Return Value:' , ReturnValue)
print()
# If no index is specified it returns the last value in the list.
ReturnValue = BestFriends.pop ()
print ('Return Value:' , ReturnValue)
