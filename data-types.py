#Day 1 Data Types


#Strings
print("Hello")

string1 = "Hello"
string2 = "World"
print(string1 + " " + string2)

#Lenght of a string
print(len("Hello"))

#Subscripting
print("Hello"[4])

#Number as string
print ("123" + "345")

#Integer
print(123 + 345)

#Float
#with decimal places. Divison always results in float
z = 8/3
print(z)
print(type(z))

#Boolean
#True or False

#Rounding
#round()
print(round(z, 2))

#Change int to str
b = 2
print(str(b) + " + 3 = something")

# type() to test
a = 1
print(type(a))
#add to an int
a += 1 #this will add 1 to a
print(a)

m = "hello there"
print(type(m))

# remember division always results in a float
o = 7 / 4
print(o)
print(type(o))
# convert a float to int
print(int(o))

#f-strings mix types
number_as_int = 1234
text_as_str = "Hello There"
print(f"{text_as_str} is a string and {number_as_int} is an int.")

# % to print just the remainder
# Test if a number divides evenly into another
d = 7 % 2
print(f"The remainder of 7/2 is: {d}")
d = 4 % 2
print(f"The remainder of 4/2 is: {d}")
