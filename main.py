from os import urandom
from csv import DictReader
# raise IOException if open("keycodes.csv") == False

def readKeycodes():
    # Import ASCII keycodes from keycodes.csv
    keycodes = {}
    try:
        with open("keycodes.csv", "r") as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                keycodes[str(row["keycode"])] = str(row["char"])
    except FileNotFoundError:
        print("keycodes.csv was not found. Please run scrapeKeycodes.py")
        exit()

    return keycodes

# Characters that typically can't be used in passwords
invalidChars = list(range(0,33))
invalidChars.append(127)
keycodes = readKeycodes()

# Get password length
while True:
    length = input("Enter pasword length (ENTER for 16): ")

    if length == "":
        length = 16
        break

    else:
        try:
            length = int(length)
            if length < 1:
                print("Length must be >0")
            else:
                print("Valid length")
                break
        except ValueError:
            print("Error length must be number. Retry")
print("")
# Output 4 passwords
for x in range(4):
    password = ""
    for i in range(length):
        valid = False
        while not valid:
            keycode = int.from_bytes(urandom(1), byteorder="little")
            # Urandom generates a minimum of 1 byte so may be more than needed
            valid = True if keycode>32 and keycode<127 else False

        # Add ASCII character represented by keycode using the keycode dictionary
        password += str(keycodes[str(keycode)])
    print(f"Password {x+1}: {password}")
