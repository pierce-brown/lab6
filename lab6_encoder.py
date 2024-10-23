# Pierce Brown

def encode(password):
    encoded = ''
    for val in password:
        encoded += str((int(val) + 3)%10)
    return encoded

def decode(encoded_password):
    # decoder logic
    pass

def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        sel = int(input("Please enter an option: "))

        if 0 < sel < 4:
            if sel == 1:
                password = input("Please enter your password to encode: ")
                if(password.isdigit() and len(password) == 8):
                    encoded_password = encode(password)
                    print("Your password has been encoded and stored!")
                else:
                    print("Invalid password, please enter an 8-digit number.")
            if sel == 2:
                # prints encoded and decoded password
                pass
            if sel == 3:
                break
        else:
            print("Please input a valid selection.")

if __name__ == '__main__':
    main()
    quit()