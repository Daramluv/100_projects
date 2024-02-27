#Tip Calculator

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("Hou much tip would you like to give? 15, 18, 23? "))
people = int(input("How many people to split the bill? "))

total_tip = total_bill * (percent_tip/100)
total_amount = total_bill +total_tip
each_person = total_amount / people

print(f"each person should pay: ${each_person}")