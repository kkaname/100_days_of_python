from caesar_ciper_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_number, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_number *= -1

    for word in original_text:
        if word not in alphabet:
            output_text += word
            continue

        shifted_position = alphabet.index(word) + shift_number
        shifted_position %= len(alphabet)
        output_text +=  alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

    
option = "yes"
while(option == "yes"):
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt: ").lower()
    text = input("Type you message: \n").lower()
    shift =  int(input("Type the shift number: "))
    if (direction == "encode" or direction == "decode"):
        caesar(text, shift, direction)
    else:
        print("You have entered the wrong option, please try again.")
    #ask the user that does they want to encode/decode again
    option = input("Type 'yes' if you want to go again.x Otherwise type 'no': ").lower()
    print("\n")

