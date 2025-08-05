from caesar_ciper_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(text):
    encrypted_text = []
    for word in text:
        if(word == " "):
            encrypted_text += " "
            continue
        encrypted_text += alphabet[alphabet.index(word) + shift]

    print("Here's the encoded result: ", end='')
    for word in encrypted_text:
        print(word, end='')
    print("\n")

def decryption(encrypted_text):
    decrypted_text = []
    for word in encrypted_text:
        if(word == " "):
            decrypted_text += " "
            continue 
        decrypted_text  += alphabet[alphabet.index(word) - shift]

    print("Here's the decoded result: ", end='')
    for word in decrypted_text:
        print(word, end='')
    print("\n")

    
option = "yes"
while(option == "yes"):
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt: ").lower()
    text = input("Type you message: \n").lower()
    shift =  int(input("Type the shift number: "))
    #
    if (direction == "encode"):
        encryption(text)
    elif (direction == "decode"):
        decryption(text)
    else:
        print("You have entered the wrong option, please try again.")
    #ask the user that does they want to encode/decode again
    option = input("Type 'yes' if you want to go again.x Otherwise type 'no': ").lower()

