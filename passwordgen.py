try:
    import random
    from time import sleep
except:
    print("there is an error while opening modules please install them or check source code")
    exit()
print("Welcome to password generator, this code will generate code as much as you need\n thanks for using my code\nPublisher: AlPHA \nVersion: 1.0.0")
sleep(2)

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','!','@','#','$','&','?','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','1','2','3','4','5','6','7','8','9','0','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letter_wo_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def enter():
 import random

password_len = int(input("Enter the length of the password: "))

UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']


COMBINED_LIST = DIGITS + UPPERCASE + LOWERCASE + SPECIAL
password = "".join(random.sample(COMBINED_LIST, password_len))

print(password)
