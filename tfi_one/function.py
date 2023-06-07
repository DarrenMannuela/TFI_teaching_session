# Initializing a function

# Initializing a function
def say_hello():
    print("Hello")

# We can call the function say_hello
say_hello()


# We can also return values from function calls

# Say we have the length and height of a triangle
length = 10
height = 8


# We can make functions take in parameters 
def triangle_area(length, height):
    area = 1/2*(length*height)
    return area

area = triangle_area(length, height)

print(f"The area of the traingle is {area}")