# Looping statements is used to repeatedly perform a block of operations.
# For loop: It is used to iterate over a sequence starting from first value to the last.
Numbers = [1,2,3,4,5]
for number in Numbers:
    print (number , end=' ')
print()
print()

# While loop: It is used to repeatedly execute a block of statements as long as the condition mentioned holds true.
length = 1
while length <= 3:
    print ("Value of the length is" , length )
    length = length + 1
print()

# Nested loop: A loop within another loop is called as Nested loop.
adj = ["red" , "big" , "tasty"]
fruits = ["apple" , "banana" , "cherry"]
for x in adj:
    for y in fruits:
        print (x , y)
print()

# Break: Break is used to stop a loop from further execution.
length = 1
while length > 0:
    if length == 3:
        break
    print ("Length =" , length)
    length = length + 1
print()

# Continue: It is used to skip a particular iteration.
length = 1
while length <= 4:
    if length == 2:
        length = length + 1
        continue
    print ("Length =" , length)
    length = length + 1
print ()

# Else: The block os statement in else block is executed if the break statement in the loop was executed.
length = 1
while length <= 3:
    if length == 5:
        break
    print ("Length =" , length)
    length = length + 1
else:
    print ("Break statement was not executed")
