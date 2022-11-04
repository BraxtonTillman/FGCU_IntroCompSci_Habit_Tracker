#Braxton Tillman
''' Habit Tracker Program that will take inputs from the user
and assign them to habits that the user can then track either in a row
or on a calendar basis'''

habitlist = []

def introduction():
    print("Hello there! \nThis program is designed to help you track habits that you personally create!")
    

def introductionCheck(check):
    while check < 1 or check > 5:
        check = int(input("Invalid. Please enter a number 1-5: "))
    
def habitCounter(habit):
    for count in range(habit_counter):
        habit = input("Enter Habit: ")
        habitlist.append(habit)
    
def habitCheck():
    for i in habitlist:
        if habit_counter == 1:
            daycount =input("Did you start today? Yes/No: ")
            if daycount != "Yes":
                print(i)
            else:
                print(i, "1",sep=": ")    
        elif habit_counter == 2:
            daycount =input("Did you start today? Yes/No: ")
            if daycount != "Yes":
                print(i)
            else:
                print(i, "1",sep=": ")
        elif habit_counter == 3:
            daycount =input("Did you start today? Yes/No: ")
            if daycount != "Yes":
                print(i)
            else:
                print(i, "1",sep=": ")
        elif habit_counter == 4:
            daycount =input("Did you start today? Yes/No: ")
            if daycount != "Yes":
                print(i)
            else:
                print(i, "1",sep=": ")
        elif habit_counter == 5:
            daycount =input("Did you start today? Yes/No: ")
            if daycount != "Yes":
                print(i)
            else:
                print(i, "1",sep=": ")
        else:
            None

introduction()
habit_counter = int(input("How many habits do you want to track? 1-5: "))
introductionCheck(habit_counter)
habitCounter(habit_counter)
habitCheck()

#Dialogue
print("Hope you have a great day!", " Stay focused!", sep='')
print("Everything below is computations not related to the program.")

#Basic Calculations (not used in program)

print(10**2) #10 to the power of 2 (Exponent)
print(5*2) #5 times 2
print("Hello There" * 10)#will type out Hello There 10 times on the same line (needs print function to display)
print(12/2) #12 divided by 2
print(6%2) #remainder of 6 divided by 2 in this case it would be 0 (% is called modulus operator)
print(17//2) #17 divided by 2 but rounded down to the nearest whole number so it would be 8
print("Hello" + "There") #concatenating hello and there 
print(2+2) #adding 2 plus 2
print(3-2) # 3 minus 2
print(habitlist)#Just a check for the list
x = 0
if x is not 0:
    print("x is not 0")
else:
    x += 1





