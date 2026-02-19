print("Password Strength Checker")

password = input("Enter a password: ")

if len(password) < 6:
    print("Weak password - too short")
elif len(password) < 10:
    print("Medium password")
else:
    print("Strong password")
