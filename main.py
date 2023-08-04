import random


def main():
    # numbers 1-100
    # random number picked
    # 5 guesses -> higher or lower
    # gives a score based on how close you were to the target
    target = random.randrange(1, 100)
    guess = int(input("Enter a number 1-100: "))
    guess_list = [guess]
    while guess != target:
        if len(guess_list) > 6:
            print("Sorry! You are out of guesses!")
            break
        if guess < target:
            print("Target number is higher!")
        else:
            print("Target number is lower!")
        print("Previous Guesses: " + str(guess_list))
        guess = int(input("Enter a number 1-100: "))
        guess_list.append(guess)
    print("The target was: " + str(target))
    if guess == target:
        print("You won!")
    else:
        print("Nice try!")
    print(str(guess_list))

if __name__ == "__main__":
    main()