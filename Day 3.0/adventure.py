print(''' __       __          .--.
(  ""--__(  ""-_    ,' .-.\        *
 "-_ __  ""--__ "-_(  (^_^))      /
    (  """--___""--__" )-'(      /
     "-__      ""---/ ,(., )__o-/,  
         """----___(.'.   /--"--'
                   ("-_"/(    /
                    \   \ \
                     `.  \ |
                       \  \/
                       ||  \
                     ,-'/`. \
                     ) /   ) \  Ojo '98
                     |/    `-.\
                              `\\''')
print("Welcom to Tressure Island, you mission is to find the tresure")
lives = 1
while lives == 1:
    direction = str(input("Will you go left or right, l or r "))
    if direction == 'r':
        lives -= 1
        print("game over")
    else:
        swim_or_wait = str(input("Will you swim or wait: s or w "))
        if swim_or_wait == 's':
            lives -= 1
            print("game over")
        else:
            door = str(input("Which door, red, yellow, or blue "))
            if door == "red" or door == "blue":
                lives - 1
                print("game over")
            elif door == "yellow":
                print("You win!")
                lives -= 1
    