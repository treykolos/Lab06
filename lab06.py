# Made by Trey Kolos
def encode(password):
    encodedpassword = ''
    for element in password:
        element = int(element) + 3 % 10
        encodedpassword = encodedpassword + str(element)
    return encodedpassword


#decode function added by John McGraw
def decode(encodedpassword):
    decodedpassword = ''
    for element in encodedpassword:
        element = abs(int(element) - 3)
        decodedpassword = decodedpassword + str(element)
    return decodedpassword


def main():
    useroption = 0
    while not useroption == 3:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        useroption = int(input('Please enter an option: '))
        encodedpassword = ''
        decodedpassword = ''
        if useroption == 1:
            decodedpassword = str(input('Please enter your password to encode: '))
            encodedpassword = encode(decodedpassword)
            print("Your password has been encoded and stored!\n")
        elif useroption == 2:
            if encodedpassword == '':
                encodedpassword = str(input("Please enter your password to decode: "))
                decodedpassword = decode(encodedpassword)
                print(
                    "The encoded password is " + encodedpassword + ", and the original password is " + decodedpassword + ".")
            else:
                print("The encoded password is " + encodedpassword + ", and the original password is " + password + ".")
        elif useroption == 3:
            break

if __name__ == "__main__":
    main()
