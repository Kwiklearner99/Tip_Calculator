total_bill = float(input("What is the total bill?: "))
# This will request the payor to input the percentage the waiter will be paid
tip_pct = float(input("What % tip would you like to give?: "))
# The tax is based on the 10% calculation which is converted to .10 for correct calulation
split = float(input("How many people will split the bill? "))
tax = .10
tax_bill = (total_bill * tax) + total_bill
tip_amt = tax_bill * (tip_pct/100)

#tip = total_bill*(tip_amt/100)

grand_total = tax_bill + tip_amt
payment_per_person = grand_total / split

print(
    f"Each person should pay: ${payment_per_person:.2f} and your tip was ${tip_amt:.2f}.")
print(f" Your total with tax is ${grand_total:.2f}.\n")

# This code enables party participants to divide the bill in amongs themselves
# number_of_people = int(input("How many people are splitting the bill?: "))
# This code breaks down the total bill with the tax and tip included
# grand_total = (tax + tip_amt)
# payment_per_person = grand_total / number_of_people
# print(
#     f"Your grand total is  ${grand_total }and each person owes: ${payment_per_person}")
print("Thank you for the business!")
