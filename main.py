# _BraxtonTillman_
""" Habit Tracker Program that will take inputs from the user
and assign them to habits that the user can then track either in a row
or on a calendar basis"""

# Lists
habit_list = []
no_list = ['No', 'no']
yes_list = ['Yes', 'yes']


# Functions
def introduction():
    """
    This is a function that makes a basic introduction to help the user
    understand the program and its uses.
    """

    print(
        "Hello there! \nThis program is designed to help you track habits "
        "that you personally create!")


def habit_counter(habit_count):
    """
    This is a function that takes the user's habits and puts them into a list
    :param habit_count:
    """
    for count in range(habit_count):
        habit = input("Enter Habit: ")
        habit_list.append(habit)


def habit_check():
    """
    This is a function that takes the user input and asks if you started today
    and makes sure the user follows instructions.
    """

    for i in habit_list:
        while user_input1 == 1:
            day_count = input("Did you start today? Yes/No: ")
            if day_count in yes_list:
                print(i, "1", sep=": ")
                break
            elif day_count in no_list:
                print(i, "0", sep=": ")
                break
            else:
                print("Not a valid option.")
        while user_input1 == 2:
            day_count = input("Did you start today? Yes/No: ")
            if day_count in yes_list:
                print(i, "1", sep=": ")
                break
            elif day_count in no_list:
                print(i, "0", sep=": ")
                break
            else:
                print("Not a valid option.")
        while user_input1 == 3:
            day_count = input("Did you start today? Yes/No: ")
            if day_count in yes_list:
                print(i, "1", sep=": ")
                break
            elif day_count in no_list:
                print(i, "0", sep=": ")
                break
            else:
                print("Not a valid option.")
        while user_input1 == 4:
            day_count = input("Did you start today? Yes/No: ")
            if day_count in yes_list:
                print(i, "1", sep=": ")
                break
            elif day_count in no_list:
                print(i, "0", sep=": ")
                break
            else:
                print("Not a valid option.")
        while user_input1 == 5:
            day_count = input("Did you start today? Yes/No: ")
            if day_count in yes_list:
                print(i, "1", sep=": ")
                break
            elif day_count in no_list:
                print(i, "0", sep=": ")
                break
            else:
                print("Not a valid option.")


def int_input():
    """

    :return:
    """
    while True:
        try:
            correct = int(input("How many habits do you want to track? 1-5: "))
            while correct < 1 or correct > 5:
                correct = int(input("Invalid. Please enter a number 1-5: "))
            return correct
        except ValueError:
            print("Not a proper integer! Try it again")


# main code
introduction()
user_input1 = int_input()
habit_counter(user_input1)
habit_check()

# Dialogue
print("Hope you have a great day!", " Stay focused!", sep='')
print("Everything below is computations not related to the program.")

# Basic Calculations (not used in program)

print(10 ** 2)
# 10 to the power of 2 (Exponent)
print(5 * 2)
# 5 times 2
print("Hello There" * 10)
# will type out Hello There 10 times on the same line
# (needs print function to display)
print(12 / 2)
# 12 divided by 2
print(6 % 2)
# remainder of 6 divided by 2 in this case it would be 0
# (% is called modulus operator)
print(17 // 2)
# 17 divided by 2 but rounded down to the nearest whole number,
# so it would be 8
print("Hello" + "There")
# concatenating hello and there
print(2 + 2)
# adding 2 plus 2
print(3 - 2)
# 3 minus 2
print(habit_list)
# Just a check for the list
x = 0
if x != 0:
    print("x is not 0")
else:
    x += 1
# An if else statement that checks if x is not equal to 0
x1 = 5
if 1 < x1 < 7:
    print("42")
else:
    print("I have failed you.")
# this is an if else statement that is using the and syntax to see if the
# variable x1 is true or false based on the condition set
