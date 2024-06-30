print (" 🔒 Pixel Manipulation for Image Encryption 🔒 ")
from PIL import Image

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
  

encrypted_image = r"D:\Laptop\cyber internship\TASK2 Pixel Manipulation for Image Encryption\encrypted.jpg"
decrypted_image = r"D:\Laptop\cyber internship\TASK2 Pixel Manipulation for Image Encryption\decrypted.jpg"

print ("\nDo you want to encrypt or decrypt a message?")
program = input("Enter 'e' for encryption or 'd' for decryption: ")
if program == 'e' or program == 'E' :
    loc = input("\nEnter Image Location That You Wanna Encrypt : ")
    encrypt_image(loc, encrypted_image)
    print("\n Image Encrypted")
elif program == 'd' or program == 'D' :
    loc = input("\nEnter Image Location That You Wanna Decrypt : ")
    decrypt_image(loc, decrypted_image)
    print("\n Image Decrypted")
else:
    print("Invalid Input")

print("\n=== Code Execution Successful ===")























            
