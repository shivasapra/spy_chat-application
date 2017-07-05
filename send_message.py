from spy_details import ChatMessage, friends
from select_a_friend import select_a_friend
from steganography.steganography import Steganography


# a function is defined for sending a secret message
def send_message():
    # calling select a friend function to obtain index
    friend_choice = select_a_friend()
    original_image = raw_input("what is the name of the image?")
    output_path = "image.jpg"
    text = raw_input("what do you want to say")
    # encoding secret message in a image
    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text,True)

    # appending chat in list
    friends[friend_choice].chat.append(new_chat)
    print "your secret message is ready"
