# Step 1 Declare variables to store the string values
name = "John Smith"
address = "101 N. Main Street"
city = "AnyTown"
state = "TX"
zipCode = "11111"
unitsTaken = "19"
# Step 2 For the price per unit, declare a constant numeric variable to contain the decimal value 100.50
PRICE_PER_UNIT = 100.50
# Step 3 For the 20-unit-hour discount, declare a constant numeric variable to contain the whole number 150.
DISCOUNT = 150
# Step 4 Convert the string value for Units Taken to an integer data type and place the converted numeric value into a separate numeric variable.
intUnitsTaken = int(unitsTaken)
# Step 5 Increment the variable above by 1 so that the value 19 will now be 20.
intUnitsTaken = intUnitsTaken + 1
# Step 6 Multiply the constant variable for price per unit by the units taken and place the answer in a variable named tuition.
tuition = PRICE_PER_UNIT * intUnitsTaken
# Step 7 Subtract the constant discount value from tuition and store the answer in a variable named afterDiscount.
afterDiscount = tuition - DISCOUNT 
# Step 8 Divide the discounted tuition by 12 and store the answer in a variable named monthlyPayment.
monthlyPayment = afterDiscount / 12
print(f"Name: {name}")
print(f"Address: {address}")
print(f"City: {city}")
print(f"State: {state}")
print(f"ZIP code: {zipCode}")
print(f"The number of units taken is: {intUnitsTaken}")
print(f"The tuition before discount is ${tuition:,.2f}")
print(f"The tuition after 20-unit discount is ${afterDiscount:,.2f}")
print(f"Your monthly payment is ${monthlyPayment:,.2f}")

