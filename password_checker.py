print("Advanced Password Strength Checker")

password = input("Enter a password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if len(password) < 8:
    print("Weak password - must be at least 8 characters.")
elif not has_upper:
    print("Weak password - add at least one uppercase letter.")
elif not has_lower:
    print("Weak password - add at least one lowercase letter.")
elif not has_digit:
    print("Weak password - add at least one number.")
elif not has_special:
    print("Weak password - add at least one special character.")
else:
    print("Strong password!")
