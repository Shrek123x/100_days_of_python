weight = int(input("Please enter your weight in KG: "))
height = int(input('please enter your height in cms: '))
bmi = weight / height ** 2
simplified_bmi = bmi * 10000
print(f"You BMI is {simplified_bmi}")