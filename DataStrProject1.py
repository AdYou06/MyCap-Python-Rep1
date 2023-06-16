#task 1


import math # the program imports the math module to access the value of pi (math.pi)

# Accept the radius from the user
r=float(input("Input the radius of the circle: "))

# Calculate the area of the circle
a= math.pi*(r**2)

# Print the result
print("The area of the circle with radius ",r,"is: ",a)



#task 2


# Accept the filename from the user
filename= input("Input the Filename: ")

# Split the filename by dot and extract the last element as the extension
ext= filename.split('.')

# Print the result
print("The extension of the file is : ",ext[1])
