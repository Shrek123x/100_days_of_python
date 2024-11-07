
print("Welcome to the tip calculator, How much would you like to Tip")
total_bill = float(input("what was the total bill"))
tip_perc = float(input("How much would you like to tip: 10, 12, 20, or custom percent: "))
tip_amount = tip_perc / total_bill * 100
amount_of_people = int(input("Are we spliting the bill with others, if so how many people: "))
total_amount_including_tip = tip_amount + total_bill
final_amount_per_person = total_amount_including_tip / amount_of_people
print(f"Each party will have to pay: {final_amount_per_person}")

print(type(1))
print(type(True))
print(type(12.21))
print(type("cat"))
# type casting
print(type(int("123")))