import random as rd

print("Welcome to the CPU number guesser.")
rangenum = int(input("Enter the highest number in the guessing range for the CPU to use (0 to 'Your input'): "))
unum = int(input("Enter the a number that you would like the CPU to guess: "))
print(f"You chose, {unum}")

def cpu_guess(x):
    lower = 0
    upper = x
    uinput = ''
    while uinput != 'c':
        if lower != upper:
            guess = rd.randint(lower, upper)
            print(f"Cpu will be guessing anywhere from {lower} to {upper}.")
        else:
            guess = lower
        uinput = input(f"Is the number: {guess}, lower (L), higher (H), or the correct number (C)?: ").lower()
        if uinput == 'h':
            upper = guess - 1
        elif uinput == 'l':
            lower = guess + 1
    print(f"Cpu has guessed your number, {guess}.")

cpu_guess(rangenum)
