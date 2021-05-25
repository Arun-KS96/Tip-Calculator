#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))

amount_to_be_paid = (total_bill / split_bill) * (1 + (percentage/100))
final_amount = round(amount_to_be_paid,2)
final_amount = "{:.2f}".format(amount_to_be_paid)
print(f"Each person should pay: ${final_amount}")
