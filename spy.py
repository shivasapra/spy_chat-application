# spy details imported from spy _details.py
from spy_details import spy, Spy, ChatMessage,maintain
# importing libraries
from datetime import datetime
from steganography.steganography import Steganography


# list of status messages
status_messages = ["die with memories not with dreams", "busy", "despacito", "Goooooogle!!!, i'm on my way"]
# list of friend
friends = []


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

# function defined to read chat
def read_chat():
    read_for = select_a_friend()
    from colorama import init,Fore
    #initializing
    init(autorest = True)
    for chat in friends[read_for].chat:
        if chat.sent_by_me:
            print '[%s] [%s], %s %s    :   %s' % (chat.time.strftime("%d %B %Y"), Fore.BLUE + chat.time.strftime("%H:%M:%S") , Fore.RED + spy.name,  Fore.BLACK + "said" ,chat.message)
        else:
            print '[%s] [%s], %s %s %s : %s' % (chat.time.strftime("%d %B %Y"), Fore.BLUE + chat.time.strftime("%H:%M:%S"), Fore.RED + friends[read_for].salutation, Fore.RED + friends[read_for].name,Fore.Black + "Recieved",chat.message)


# function defined for taking details from spy
def spy_detail():
    global spy
    spy = Spy(" "," ",0,0.0)
    # taking name from user if invalid taking name again
    temp = 0
    while temp == 0:
        spy.name = raw_input("\n****************\nEnter Name")
        try:
            if type(int(spy.name)) == int:
                temp = 0
                exit(temp == 0)
        except:
            temp = len(spy.name)
            exit(temp == 0)
        # taking valid salutation
    salutation = ' '
    while salutation != 'mr.' and salutation != 'ms.':
        salutation = raw_input("****************\nwhat should we call (mr.or ms.)")
    spy.salutation = salutation
    spy.name = spy.salutation + spy.name
    # taking age and checking if it is in right format or not
    temp = 1
    while temp:
        spy.age = raw_input("****************\nplease enter age")
        try:
            if type(int(spy.age)) == int:
                temp = 0
                spy.age = int(spy.age)
        except:
            print "\n!!!!!!!!!!!!!!!\nenter carefully\n!!!!!!!!!!!!!!!\n"
            temp = 1
        # taking spy_rating and checking it
    temp = 1
    while temp:
        spy.rating = raw_input(
            "****************\nplease enter spy rating (out of 10)")
        print "****************"
        try:
            if type(float(spy.rating)) == float:
                temp = 0
                spy.rating = float(spy.rating)
        except:
            print "\n!!!!!!!!!!!!!!!\nenter carefully\n!!!!!!!!!!!!!!!\n"
            temp = 1
    spy.is_online = True
    if spy.rating >= 9.0:
        print " \nyou seems to be excellent"
    elif 9.0 > spy.rating >= 7.0:
        print "\nyou seems to be good"
    elif 7.0 > spy.rating >= 5.0:
        print "\nyou seems to be average"
    else:
        print "\nyou seems to be ok"
    # returning details of spy
    return spy


# defining a function for selecting a friend
def select_a_friend():
    if len(friends) > 0:
        print "\n*********************" \
              "\nhere are your friends" \
              "\n*********************"
        for spy in friends:
            print "*****************************************************"
            print "% s aged % d with rating % f is online" % (spy.name, int(spy.age), float(spy.rating))
            print "*****************************************************"
        item_number = 1
        for spy in friends:
            print '%d. %s' % (item_number, spy.name)
            item_number = item_number + 1
        index = int(raw_input('choose option')) - 1
        return index
    else:
        print("\n!!!!!!!!!!!!!!!!!!!"
              "\nyou have no friends"
              "\n!!!!!!!!!!!!!!!!!!!")


# function to add a friend
def add_friend():
    global Spy
    new_friend = Spy(" "," ",0,0.0)
    new_friend.name = raw_input("enter your friend's name")

    new_friend.salutation = raw_input("are they mr. or ms. or any other? : ")

    new_friend.name = new_friend.salutation + new_friend.name

    new_friend.age = raw_input("enter age")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age >12 and new_friend.age <50 and new_friend.rating >= spy.rating:
        friends.append(new_friend)

    else:
        print "sorry Invalid entry,We can't add your friend"

    return len(friends)


# function  for adding status
def add_status(current_status_message):
    # checking if there is any current status message or not
    if current_status_message != None:
        print "\n*******************************\n your current status message is" \
              + " " + current_status_message + "\n*******************************"

    else:
        print "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" \
              "\n you don't have any status currently" \
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    temp = 1
    while temp:
        # asking if user wants to choose from older status or not
        default = raw_input("\n***********************************************\n"
                            "do you want to select from the older status (y/n)"
                            "\n***********************************************")
        if default.upper() == 'N':
            temp = 0
            new_status_message = raw_input("\n*********************\nenter status message")
            print "*********************"
            if len(new_status_message) > 0:
                updated_status_message = new_status_message
                status_messages.append(updated_status_message)
                return updated_status_message

        elif default.upper() == 'Y':
            temp = 0
            item_position = 1
            for message in status_messages:
                print "\n" + str(item_position) + " " + message
                item_position = item_position + 1
            message_selection = int(raw_input("\nchoose a status"))
            if len(status_messages) >= message_selection:
                updated_status_message = status_messages[message_selection - 1]
                return updated_status_message


# function for printing menu and calling other functions according to user's choice
def start_chat(spy):
    current_status_message = None
    if 12 < spy.age < 50:
        print "\n\n\n**************************"
        print "welcome " + spy.name + "\n age: " + str(spy.age) + " \n rating: " + str(spy.rating)
        print "**************************"
        temp = 1
        while temp:
            menu_choice = int(raw_input("\n**********what do you want to do?********** \n "
                                        "1. update a status \n 2.Add a friend \n "
                                        "3. send secret message to a friend \n"
                                        "4. read a secret message\n"
                                        "5. read chat history\n"
                                        "6. exit application\n"
                                        "**********************************************\n"))
            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
                print "\n******************************"
                print "your status message is"
                print current_status_message
                print "**********************************"
            elif menu_choice == 2:
                no_of_friends = (add_friend())
                print "\n**********" + str(no_of_friends) + " friend/s added" + "**********"
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()
            elif menu_choice == 5:
                read_chat()
            elif menu_choice == 6:
                print "thanks"
                exit()
            else:
                print "\n!!!!!!!!!!!!!!!\nenter carefully\n!!!!!!!!!!!!!!!"
                temp = 1
    else:
        print "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" \
              "\nyou are not eligible for a spy in this age" \
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


# program starts from here
print("***************\n welcome!!!!.... \n***************")

proceed = 1
while proceed:
    # checking while user want to proceed with default user or not and taking action according to it
    proceed = raw_input("\nwant to proceed with default user (y/n)")
    if proceed.lower() == 'y':
        proceed = 0
        start_chat(spy)

    elif proceed.lower() == 'n':
        spy = spy_detail()
        proceed = 0
        start_chat(spy)
    else:
        print "\n!!!!!!!!!!!!!!!\nENTER CAREFULLY\n!!!!!!!!!!!!!!!"
