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
    print("please enter your Username and password")
    username = input("Username: ")
    password = input("Password: ")
    #password and username for starting code
    if username == "amir" and password == "83":
        print("Correct credentials")
    else:
        return exit()
def pass_wo_char():
    for i in range(pass_num):
        password_i = ''
        for p in range(requirements_len):
            password_i += random.choice(letter_wo_char)
        print(password_i)
def pass_w_len():
    for i in range(pass_num):
        password_i = ''
        for p in range(requirements_len):
            password_i += random.choice(letter)
        print(password_i)
def password():
    global requirements_len,pass_num,requirements_sp
    requirements_sp = input("Do you want special characters (#,@,$,!)???? ")
    sleep(0.3)
    requirements_len = int(input("What's the length of password you want??? \n***We recommend more than 12 because of your safety!"))
    sleep(0.3)
    pass_num = int(input("How many passwords you want???"))
    sleep(0.3)
    if requirements_sp == 'y' or requirements_sp == 'yes':
        pass_wo_char()
    elif requirements_len > 5:
        pass_w_len()
    else:
        return exit()
try:
    enter()
    password()
    sleep(5)
except:
    print("there is an error in code I can't process the code\nplease check source code")
    exit()
