#Data Types

#string
# print("Hello"[4])

#Integer
# print(123+345)

#float
# 3.14159

#boolean
# True
# False

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")


# challenge 1
# two_digit_number = input("Type a two digit number: ")

# a=two_digit_number[0]
# b=two_digit_number[1]

# new_a=int(a)
# new_b=int(b)

# print(new_a+new_b)

# 3+5
# 7-4
# 3*2
# 6/3
# 2**3

# PEMDAS  left symbol is always prioritized code is read left to right
# ()
# **
# */
# +-

# print(3 * 3 + 3 / 3 - 3)

#challenge2 both bmi variable will produce the same result
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# new_height = float(height)
# new_weight = int(weight)

# bmi = new_weight / (new_height * new_height) 
# bmi = new_weight / new_height ** 2

# print(int(bmi))


# // is a integer sing / is a float
# print(8 // 3)
# print(round(8 / 3, 2))


# F-string example
# score = 0
# height = 1.8
# isWinning = True

# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


#challenge 3

# age = input("What is your current age? ")
# new_age = int(age)
# final_age = int(90)
# years_left = final_age - new_age

# days = round(years_left * 365)
# weeks = round(years_left * 52)
# months = round(years_left * 12)

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

a = int("5") / int(2.7)
print(type(a))