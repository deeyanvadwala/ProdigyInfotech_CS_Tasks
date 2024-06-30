print (" 🔒 Code To Implement Ceasar Cipher 🔒 ")
def caesar_cipher(text, shift, program):
    result = ""
    shift = int(shift) 
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if program == 'e':
                result_char = chr((ord(char) - start + shift) % 26 + start)
            elif program == 'd':
                result_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Invalid action. Use 'e' to encrypt or 'd' to decrypt")
            result += result_char
        else:
            result += char
    return result

print ("\nDo you want to encrypt or decrypt a message?")
program = input("Enter 'e' for encryption or 'd' for decryption: ")
if program == 'e' or program == 'E' :
    pt = input("\nEnter Text You Want To Encrypt = ")
    shift = input("\nEnter Shift Value = ")
    result = caesar_cipher(pt, shift, 'e')
    print("\nEncrypted Message:", result)
elif program == 'd' or program == 'D':
    ct = input("\nEnter Text You Want To Decrypt = ")
    shift = input("\nEnter Shift Value = ")
    result = caesar_cipher(ct, shift, 'd')
    print("\nDecrypted Message:", result)
else:
    print("Invalid Input")
print("\n=== Code Execution Successful ===")

