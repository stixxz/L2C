# input() Will get use input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name? \n"))
# prints the input but count the length of the string
print(len(input("What is your name? ")))

#deccleration of variables and recalling said variables
name = ("Jack")
print(name)

name = "Angela"
print(name)

name = input("What is your name? ")
length = len(name)
print(length)


#code challenge
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
temp = a
a = b
b = temp
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)