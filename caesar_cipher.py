#KG caesar cipher assignment

def encode_message(message, shift):
    result = ""

    for char in message:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decode_message(message, shift):
    return encode_message(message, -shift)

while True:
    try:
        shift = int(input("I need a number so I can make the message secret. What number do you want?: \n"))
    except:
        print("Put a number")
    else:
        break

while True:
    choice = input("Do you want to encode a message (1) or decode a message (2)? \n")
    
    if choice == "1":
        message = input("What is your message? \n")
        encode = encode_message(message, shift)
        print(encode)
    elif choice == "2":
        message = input("What are you decoding? \n")
        decode = decode_message(message, shift)
        print(decode)
    else:
        print("That's not an option, try again.")