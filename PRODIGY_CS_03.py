print("🔒 Password Complexity Checker 🔒")
import string

def check_pwd():
    password = input("\nEnter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength == 3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    print('\nYour password has: ')
    print(f"\n{lower_count} lowercase characters")
    print(f"\n{upper_count} uppercase characters")
    print(f"\n{num_count} numeric characters")
    print(f"\n{wspace_count} whitespace characters")
    print(f"\n{special_count} special characters")

    print(f"\nPassword Strength: {strength}")
    print(f"\nHint: {remarks}")

def ask_pwd(another_pwd=False):
    while True:
        if another_pwd:
            choice = input('\nDo you want to enter another pwd (y/n): ')
        else:
            choice = input('\nDo you want to check a password (y/n): ')
        
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid choice, Try Again')

if __name__ == '__main__':
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
