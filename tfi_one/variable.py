a = 1 # integer data type
b = "Hello" # string data type
c = "1" # this is 1 but in the string data type
d = 1.0 # float data type
e = 1.00 # double data type
f = True # boolean data type (True, False)

print("\n This is the int data type: " + str(a) + f", a is: {type(a)}\n")
print("\n This is the string data type: " + b + f", b is: {type(b)}\n")
print("\n This is also the string data type: " + c + f", c is: {type(c)}\n")
print("\n This is also the float data type: " + str(d) + f", d is: {type(d)}\n")
print("\n This is also the decimal data type: " + str(e) + f", e is: {type(e)}\n")
print("\n This is also the boolean data type: " + str(f) + f", f is: {type(f)}\n")

a = c # a now has the value stored in the variabe at c

print("\n a now holds the value of the variable at c: " + a + f", a is: {type(a)}\n")