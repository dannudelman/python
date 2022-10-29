import random
from random import randint
from time import sleep
balanc = 0
money_entered = int(input("insert money to play a game (1 game = 10$) : $ "))
balanc = money_entered
change = 0.0
first_cube = 0
seconde_cube = 0
while money_entered < 10:
    money_entered = int(input(f"you need to insert 10 dolars or above \n try again : $ "))

round = money_entered // 10
if money_entered % 10 != 0:
    change = money_entered % 3
    print(f"you can play {round.__round__()} times\n ")
    print(f"you change is {change}$\n ")
else:
    print(f"you can play {round.__round__()} times\n ")

for i in range(int(round)):
    balanc -= 10
    print(f"round number {i + 1}\n"
          f"money entered : {money_entered}$\n"
          f"your blance : {balanc}$\n")
    print("cubes getting ready..\n")
    sleep(3)
    first_cube = random.randint(1,6)
    second_cube = random.randint(1,6)
    if first_cube != 1 and second_cube != 2 and first_cube != seconde_cube:
        print(f"cube 1 = {first_cube}\n"
              f"cube 2 = {second_cube}\n"
              f"sorry you didnt win nothing\n"
              f"your balance is {balanc}$\n")
    if first_cube == second_cube:
        if first_cube == 6:
            balanc += 1000
            print(f"cube 1 = {first_cube}\n"
                  f"cube 2 = {second_cube}\n"
                  f"you won 1,000$\n"
                  f"your balance is {balanc}$\n")
        else:
            balanc += 100
            print(f"cube 1 = {first_cube}\n"
                  f"cube 2 = {second_cube}\n"
                  f"you won 100$\n"
                  f"your balance is {balanc}$\n")
    elif first_cube == 1:
         if second_cube == 2:
               balanc += 60
               print(f"cube 1 = {first_cube}\n"
                      f"cube 2 = {second_cube}\n"
                      f"you won 60$\n"
                      f"your balance is {balanc}%\n")
         else:
            balanc += 20
            print(f"cube 1 = {first_cube}\n"
                  f"cube 2 = {second_cube}\n"
                  f"you won 20$\n"
                  f"your balance is {balanc}$\n")
    elif second_cube == 2:
         balanc += 40
         print(f"cube 1 = {first_cube}\n"
               f"cube 2 = {second_cube}\n"
               f"you won 40$\n"
               f"your balance is {balanc}$\n")
