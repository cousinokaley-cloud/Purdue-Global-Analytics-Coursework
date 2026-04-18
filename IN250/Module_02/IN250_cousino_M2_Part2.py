'''

*********************************************************

****Assessment Part 2 Section 1

*********************************************************

'''

grades = int(input("Enter number of grades to average: "))
counter = 1
total = 0
while counter <= grades:
    grade = int(input("Enter a grade: "))
    total = total + grade
    counter = counter + 1
average = total / grades
print("Total of all grades is", total)
print("Class average is", average)

'''

*********************************************************

****Assessment Part 2 Section 2

*********************************************************

'''   
    
k = 5
while k >= 1:
    i = 0
    while i <= 10:
        print("k =", k, "i =", i)
        i = i + 2        
    k = k - 1     

'''

*********************************************************

****Assessment Part 2 Section 3

*********************************************************

'''

total = 0
while True:
    number = int(input("Enter a positive number to be added to the total or -1 to end."))
    if number == -1:
        break
    total = total + number
print("The sum of all numbers entered is", total)
