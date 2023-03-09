#Made by Trey Kolos
def encode(password):
    encodedpassword = ''
    for element in password:
        element = int(element) + 3 % 10
        encodedpassword = encodedpassword + str(element)
    return encodedpassword

def main():
    useroption = 0
    while not useroption == 3:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        useroption = int(input('Please enter an option: '))
        if useroption == 1:
            password = str(input('Please enter your password to encode: '))
            encodedpassword = encode(password)
            print("Your password has been encoded and stored!\n")
        elif userOption == 2:
            print("The encoded password is " + encodedpassword + ", and the original password is " + password + ".")
        elif useroption == 3:
            break

    if __name__ == "__main__":
        main()