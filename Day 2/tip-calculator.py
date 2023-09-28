print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
split = input("What precentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_int = float(bill)
split_float = int(split)
split_num = split_float / 100
people_int = int(people)
split_precentage = bill_int * split_num
total_bill_tip = bill_int + split_precentage
invidual_bill = total_bill_tip / people_int
final_bill = round(invidual_bill, 2)
final_bill = "{:.2f}".format(invidual_bill)

print(f"Each person should pay: ${final_bill}")