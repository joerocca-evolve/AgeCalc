fruit_basket = ["apple", "orange", "pear", "grape", "strawberry"]

fruit_guess = input("Guess a fruit! Enter your guess below\n")

if fruit_guess in fruit_basket:
    print("\nYou guess correctly!")
else:
    print("\nThat fruit is not in the basket. Try again!")
