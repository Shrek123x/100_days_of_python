import random
random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)

random_number_0_to_10 = random.random() * 10
print(random_number_0_to_10)

another_random_float = random.uniform(1, 10)
print(another_random_float)

# head or tail program
choices = ['heads', 'tails']
print(random.choice(choices))

# lists
states = ['vic', 'nsw', 'qld']
# appending to end of the list
states.append("wa")
print(states)
#adding ite, to specific index
states.insert(2, "dw")
print(states)
# replacing an item within the lists
states[2] = 'cn'
print(states)
# we can also joing two lists togather
fav_food = ['pie', 'lamington', 'rolls']
states.extend(fav_food)
print(states)

#Who will apy the bill
people = ['bob', 'alice', 'cate']
choice = random.choice(people)
print(f"the bill will go to {choice}")
random_int = random.randint(0, 2)
print(f" the bill will go to {people[random_int]}")

#nested Lists
veg = ['lettuce', 'spinach', 'broc']
fruit = ['apples','oranges', 'lemons']
dirty_dozen = [veg, fruit]
print(dirty_dozen)