from random import randint

def roll():
    print(f"You rolled a dice, it lands on {randint(1,6)}.")


for i in range(10):
    roll()
