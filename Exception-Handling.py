# Exceptions are unwanted errors we receive in our program:
# Try block lets you test a block of code for errors.
try:
  print(x)
except:
  print("An exception occured")
print ()

# Many Exceptions: Here you can execute as many exception blocks you want.
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print ()

# Else: You can use the else keyword to define a block of code to execute if no errors were raised.
try:
    print ("Hello")
except:
    print ("Something went wrong")
else:
    print ("Nothing else went wrong")
print ()

# Finally: It will be executed regardless if the try block raises an error or not.
try:
    f = open ("Hello.txt")
    f.write ("I am not free today.")
except:
    print ("!!!!Something went wrong while writing to the file!!!!")
finally:
    f.close()
