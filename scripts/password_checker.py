"""
Password Strength Checker
Author: Mbali Nene
Description:
    Evaluates password strength based on length,
    uppercase letters, lowercase letters,
    numbers, and special characters.
"""

import re


def check_password_strength(password: str) -> None:
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        print("Weak Password")
    elif score == 3 or score == 4:
        print("Moderate Password")
    else:
        print("Strong Password")


def main():
    password = input("Enter a password to check: ")
    check_password_strength(password)


if __name__ == "__main__":
    main()
