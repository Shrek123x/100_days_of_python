# loops
# for loop
test_list = [1, 2, 3, 4, 5, 6]
for number in test_list:
    print(f"this looped {number} amount of times")

deposits = [129, 153, 23, 53, 21]
total = sum(deposits)
print(total)
# same funtion but for a for loop
sum = 0
for deposit in deposits:
    sum += deposit
    print(sum)
# max function with for loop
max_number = 0
for num in deposits:
    if num > max_number:
        max_number = num
print(max_number)

# for loops with range(start, end_jsut_before, steps) function
#The Gauss Challenge
total = 0
for i in range(0, 101):
    total += i
print(total)

