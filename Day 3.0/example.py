# bath tub water level
waterLevel = int(input("Please enter the water level of the bath tub: "))
if waterLevel >= 80:
    print("draining water now")
elif waterLevel < 80:
    print(f"Keep filling the water, it needs {80 - waterLevel} more liters")
else:
    pass

# Am i tall enough to ride the rollercoster
minimumHeight = 120
ticket_price = 12
photo_price = 3
userHeight = int(input("Please eneter your height in cm's: "))
user_age = int(input("How old are you: "))
photo_to_be_take = str(input(f"Would you like a photo for ${photo_price}, y/n"))
if photo_to_be_take == 'y':
    ticket_price += photo_price
elif photo_to_be_take == 'n':
    pass
if userHeight >= minimumHeight:
    if user_age >= 18:
        print(f"You are {userHeight} cm's tall meaning you can ride this rollercoaster for ${ticket_price}")
    elif user_age >= 12 and user_age < 18:
        print(f"You are {userHeight} meaning you can ride this rollercoaster for ${ticket_price - 5}")
    else:
        print(f"You are {userHeight} meaning you can ride this rollercoaster for ${ticket_price - 7}")
else:
    print(f"Sorry you are {minimumHeight - userHeight} CM to short to rise the rollercoaster")

#checking for even or odd numbers
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f"The number: {number} is even")
else:
    print(f"the number: {number} is odd")

#BMI calculator with Interpretations
weight = int(input("Please enter your weight in KG's: "))
height = int(input("Please enter your height in CM's: "))
bmi = weight / (height ** 2)
bmi = bmi * 10000
if bmi < 18.5:
    print(f"underweight {bmi}")
elif bmi <= 25.0:
    print(f"normal weight {bmi}")
else:
    print(f"Overweight {bmi}")







