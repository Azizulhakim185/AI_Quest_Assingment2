import random

def main():
    print("Welcome to the number game:")
    print("The program will automatically generate a number between 1 to 10.")
    num = random.randint(1, 10)
    f = 0
    while True:
        guess = int(input("Enter the number: "))
        f += 1
        if guess < num:
            print("Too low, try again.")
        elif guess > num:
            print("Too high, try again.")
        else:
            print("Your guess is correct!")
            print(f"Your attempt number is {f}.")
            break

if __name__ == "__main__":
    main()
