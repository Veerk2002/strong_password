# # create a strong password with the use of if else:
print("Welcome to create a strong password!!!","\n")
l=int(input("enter the length of password: "))
upper=input("enter your first name in upper case letter: ")
if upper>="A" and upper<="Z":
    print()
    lower=input("enter your last name in lower case letter:  ")
    if lower>="a" and lower<="z":
        print()
        schar=input("enter the special character: ")
        if schar=="@" or schar=="#":
            print()
            num=int(input("enter the digit: "))
            if num>=0:
                print()
                password=(upper+lower+schar+str(num))
                if len(password)==l:
                 print(password)
            else:
                print("enter the length pls")
        else:
            print("it is not special character")
    else:
        print("enter the lower case latter")
else:
    print("enter the upper case latter")