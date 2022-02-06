import string
import random
import time

while True:
    try:
        usable = string.ascii_letters         # A string of usable characters
        length = int(input("How long should the password be? "))
        num = input("Use numbers in the password? y or n ").lower()
        if num not in ('y', 'n'):
            raise ValueError                  # Makes sure the values are valid
        if num == 'y':
            usable += string.digits           # Adding to usable char set

        symbols = input("Use Symbols? y or n ").lower()
        if symbols not in ('y', 'n'):         # Same as above
            raise ValueError
        if symbols == 'y':
            usable += string.punctuation
        break                                 # Stops loop if all values are valid

    except ValueError:                        # Allows loop until all valid values are entered
        print("\nPlease enter valid values.\n")
        time.sleep(1)


def genString(charSet, length=6):             # Returns the generated password
    x = []
    for i in range(length):
        x.append(charSet[random.randint(0, len(charSet) - 1)])
    return "".join(x)


if __name__ == "__main__":
    print("Password : " + genString(usable, length))
