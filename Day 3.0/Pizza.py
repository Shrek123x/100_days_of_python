print("""Welcome to swampy pizza""")
pizza_size = str(input("What size pizza would you like, s, m, or l: "))
pepperoni = str(input("Would you like pepperoni: y/n "))
extra_cheese = str(input('Would you like extra cheese: y/n '))

total_cost = 0

if pizza_size == 's':
    total_cost += 15
elif pizza_size == 'm':
    total_cost += 20
elif pizza_size == 'l':
    total_cost += 25
else:
    print("You have entered the wrong input")

if pepperoni == 'y':
    total_cost += 2
elif pepperoni == 'n':
    pass
else:
    print("you have entered the wrong input")

if extra_cheese == 'y':
    total_cost += 4
elif extra_cheese == 'n':
    pass
else:
    print("wrong input")

print(f"You'r bill is ${total_cost}")
