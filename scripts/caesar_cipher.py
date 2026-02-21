print("Caesar Cipher Encryption Tool")

message = input("Enter a message: ")
shift = int(input("Enter shift number: "))

encrypted_message = ""

for char in message:
    if char.isalpha():
        shifted = ord(char) + shift

        if char.islower():
            if shifted > ord('z'):
                shifted -= 26
            encrypted_message += chr(shifted)
        elif char.isupper():
            if shifted > ord('Z'):
                shifted -= 26
            encrypted_message += chr(shifted)
    else:
        encrypted_message += char

print("Encrypted message:", encrypted_message)
