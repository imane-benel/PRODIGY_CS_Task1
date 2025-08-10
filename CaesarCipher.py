letters= 'abcdefghijklmnopqrstuvwxyz'
def encrypt(plaintext , shift):
    encrypted=''
    for letter in plaintext:
        letter = letter.lower()
        if not letter =='':
          index= letters.find(letter)
          if index ==-1 :
            encrypted += letter
          else:
            new_index= index + shift
            if new_index >= 26:
               new_index -= 26
            encrypted += letters[new_index]
    return encrypted

def decrypt(cipher, shift):
    plaintext=''
    for letter in cipher:
        letter = letter.lower()
        if not letter ==' ':
          index = letters.find(letter)
          if index == -1 :
            plaintext += letter
          else:
             new_index= index - shift
             if new_index < 0:
                new_index += 26
             plaintext += letters[new_index]
    return plaintext

print ("*********Caesar cipher*********")
message = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))
choice = input ("enter 'encrypt' to encrypt or 'decrypt' to decrypt ").lower()

if choice =='encrypt':
    encrypted = encrypt(message,shift)
    print(f"your message encrypted is {encrypted}")
else:
    plaintext = decrypt(message,shift)
    print(f"your message encrypted is {plaintext}")
