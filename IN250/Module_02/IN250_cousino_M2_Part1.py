"""

*********************************************************

****Assessment Part 1 Section 1

*********************************************************

"""

value1 = int(input("Enter first integer: "))
value2 = int(input("Enter second integer: "))
if value1 == value2:
    print(value1, "==", value2)
if value1 != value2:
    print(value1, "!=", value2)
if value1 < value2:
    print(value1, "<", value2)
if value1 > value2:
    print(value1, ">", value2)
if value1 <= value2:
    print(value1, "<=", value2)
if value1 >= value2:
    print(value1, ">=", value2)

"""

*********************************************************

****Assessment Part 1 Section 2

*********************************************************

"""

grade = int(input("Enter a grade: "))
if grade >= 60:
    print("Congratulations, you passed.")
else:
    print("Sorry, you failed.")

"""

*********************************************************

****Assessment Part 1 Section 3

*********************************************************

"""

month = int(input("Enter a number 1 through 12: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Error: Invalid month number.")

"""

*********************************************************

****Assessment Part 1 Section 4

*********************************************************

"""

day = int(input("Enter a number 1 through 7: "))
match day:
          case 1:
              print("Sunday")
          case 2:
              print("Monday")
          case 3:
              print("Tuesday")
          case 4:
              print("Wednesday")
          case 5:
              print("Thursday")
          case 6:
              print("Friday")
          case 7:
              print("Saturday")
          case unknown_command:
              print("Error: Invalid day number.")
