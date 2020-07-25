# Conditional Statements are block of statements whose execution depends upon the condition.
# There are 4 types of conditional statements : If , If-Else , If-Elif-Else , Nested If

# If: Here,the block of Statements gets executed when the condition mentioned is true.
distance = 1000
if distance==1000:
    print ("Distance is 1000")
print()

# If-Else: Here,block of ststements under if loop is executed when the condition is true.When the condition is false,else loop is executed.
distance = 200
if distance <=100:
    print ("Distance is less than or equal to 100")
else:
    print ("Distance is greater than 100")
print()

# If-Elif-Else: Here,multiple 'if' statements are executed one after another.When all conditions are false,else loop is executed.
distance=500
if distance <=100:
    print ("Distance is less than or equal too 100")
elif distance <=200:
     print ("Distance is less than or equal too 200")
elif distance <=300:
    print ("Distance is less than or equal too 300")
else:
    print ("Distance is greater than 300")
print()

# Nested If: An if statement within another if statement is called is nested-if statement.
distance=50
if distance <100:
    if distance ==50:
        print ("Distance is 50")
