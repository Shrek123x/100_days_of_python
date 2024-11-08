import random
chars = list("qwertyuioplkjhgfdsazxcvbnm")
num = list('1234567890')
special_char = list("!@#$%^&*()_+")
char_length = int(input("how many characters would you like: "))
num_length = int(input("How many numbers would you like"))
special_char_length = int(input("How many special characters would you like "))
def generate(chars_length, num_length, special_char_length):
    password_chars = []
    password = []
    for i in range(0, num_length):
        password_chars.append(random.choice(num))
    for i in range(0, chars_length):
        password_chars.append(random.choice(chars))
    for i in range(0, special_char_length):
        password_chars.append(random.choice(special_char))
    for i in password_chars:
         password.append(random.choice(password_chars))
    #print(password_chars)
    random.shuffle(password_chars)
    password = ''
    for i in password_chars:
        password += i
    return password
    

new_password = generate(char_length, num_length, special_char_length)
print(f"Your new password is \"{new_password}\"")
