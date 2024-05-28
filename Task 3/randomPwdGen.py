import string
import random

# Function to Generate Random Passwords
def genPwd(len, useSpChar = False):
    letters = string.ascii_letters + string.digits
    if useSpChar:   # making Password strong by using Special Characters
        letters += string.punctuation
    pwd = ''.join(random.choice(letters) for _ in range(len))
    return pwd

def main():
    print("------ Password Generator ------")
    try:
        len = int(input("Enter The Length of Password: "))
        useSpChar = input("To Get Strong Password Enter 'Y' ").upper()=='Y'
        if len <= 0:
            print("Length of the Password must be Positive!!")
        else:
            pwd = genPwd(len, useSpChar)
            print("Your Random Generated Password Is ",pwd)

    except:
        print("Invalid Input.")

if __name__ == "__main__":
    main()
