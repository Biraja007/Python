# Function is a named block of reusable code that performs a specific task.
def findMaximum (NumberOne , NumberTwo):
    if NumberOne > NumberTwo:
        return NumberOne
    else:
        return NumberTwo

NumberOne=10
NumberTwo=20
greater= findMaximum (NumberOne,NumberTwo)
print (greater)
