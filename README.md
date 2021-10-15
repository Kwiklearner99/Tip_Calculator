# Tip_Calculator Challenge
# Tip Calculator Project
total_bill = float(input("What is the total bill?: "))
# This will request the payor to input the percentage the waiter will be paid
tip_pct = int(input("What % tip would you like to give?: "))
# The tax is based on the 10% calculation which is converted to .10 for correct calulation
tip_amt = total_bill * (tip_pct/100)
tax = total_bill * .10
# This code enables party participants to divide the bill in amongs themselves
number_of_people = int(input("How many people are splitting the bill?: "))
# This code breaks down the total bill with the tax and tip included
payment_per_person = (total_bill + tax + tip_amt) / number_of_people
print(f"Each person owes: ${payment_per_person}")
print("Thank you for the business!")
