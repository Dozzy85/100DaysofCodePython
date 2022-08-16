#If the bill was $150.00, split between 5 people, with 12%
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimaò place = 33.60

print("welcome to the tip calculator.")

bill=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

percentage_tip=tip/100
total_tip_ammount=bill*percentage_tip
total_bill=total_tip_ammount+bill
bill_for_person=total_bill/people
result=round(bill_for_person, 2)

print(f"Each person should pay: {result}")