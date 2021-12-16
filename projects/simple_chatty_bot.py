# Project: Simple Chatty Bot

# Stage 1: Introduce the Bot
bot_name = 'Aid'
birth_year = 2020

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}")

# Stage 2: Print Your Name
print("Please, remind me your name.")
your_name = input()
print(f"What a great name you have, {your_name}!")

# Stage 3: Guess Age Feature
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5, and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")

# Stage 4: Learning Numbers
print('Now I will prove to you that I can count to any number you want.')
user_number = int(input())
counter = 0
while counter <= user_number:
    print(f"{counter} !")
    counter += 1
print('Completed, have a nice day!')

# Stage 5: Mulitple Choice
# See chatty_bot.py
