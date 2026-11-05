#KG caesar cipher assignment

def encode_message():



def decode_message():



while True:
    choice = input("Do you want to encode a message (1) or decode a message (2)? \n")

    if choice == "1":
        message = input("What is your message? \n")
        encode_message(message)
    elif choice == "2":
        message = input("What are you decoding? \n")
        decode_message(message)
    else:
        print("That's not an option, try again.")