from steganography.steganography import Steganography
from spy_details import ChatMessage,maintain
from select_a_friend import select_a_friend
from spy_details import friends


# function defined to read a message
def read_message():
    sender = select_a_friend()
    output_path = raw_input("what is the name of the file")
    # decoding secret text from image
    secret_text = Steganography.decode(output_path)
    if secret_text == "SOS" or secret_text == "SAVE ME" or secret_text == "HURRY!!!!":
        print "your friend is in DANGER,GET READY,WANTS YOUR HELP"
    else:
        if secret_text != None:
            print "secret message is " + " " + secret_text
            new_chat = ChatMessage(secret_text,False)
            friends[sender].chat.append(new_chat)
            print "your secret message has been saved!"
        else:
            print "no secret message in image"
            exit()

    words = len(secret_text.split())
    if words > 100:
        del friends[sender]
        print "1 friend deleted due to a lot chat"
        print "%d friends remaining" %(len(friends))

    item_number = 1
    for spy in friends:
        print '%d. %s' % (item_number, spy.name)
        item_number = item_number + 1

    maintain_words = maintain(secret_text)
