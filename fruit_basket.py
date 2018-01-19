def guess_fruit(basket):
    fruit_guess = input("Guess a fruit! Enter your guess below\n")
    while fruit_guess not in basket:
        fruit_guess = input("That fruit isn't in the basket. Try again!\n")
    print("\nYou guessed correctly!")

def main():
    fruit_basket = ["apple", "orange", "pear", "grape", "strawberry"]
    guess_fruit(fruit_basket)


main()
