secure=(('s','$'),("a","@"),('b','%'),('i','*'))
def securepassword(password):
    for a,b in secure:
        password=password.replace(a, b)
    return password
if __name__ == '__main__':
    password=input("Enter your pass word\n")
    password=securepassword(password)
    print("your secure password is :"+ password)




