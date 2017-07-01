from steganography.steganography import Steganography
from spy_details import spy
from datetime import datetime

status_messages = ["die with memories not with dreams", "busy", "despacito", "Goooooogle!!!, i'm on my way"]

friends = []


class details :
    name = " "
    salutation = " "
    age = 0
    rating = 0.0
    is_online = True


def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("what is the name of the image?")
    output_path = "image.jpg"
    text = raw_input("what do you want to say")
    Steganography.encode(original_image, output_path, text)

    class ChatMessages:
        def __init__(self,message,sent_by_me):
            self.message = message
            self.time = datetime.now()
            self.sent_by_me = True

    friends[friend_choice]['chats'].append(ChatMessages)
    print "your secret message is ready"


def read_message():
    sender = select_a_friend()
    output_path = raw_input("what is the name of the file")
    secret_text = Steganography.decode(output_path)
    print 'secret message is' + " " + secret_text

    class ChatMessages:
        def __init__(self,message,sent_by_me):
            self.message = secret_text
            self.time = datetime.now()
            self.sent_by_me = False

    friends[sender]['chats'].append(ChatMessages)
    print "your secret message has been saved!"


def read_chat():
    read_for = select_a_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s %s' % (chat.time.strftime("%d %B %Y"), 'you said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name,chat.message)


def spy_detail():
    spy = details()
    temp = 0
    while temp == 0:
        spy.name = raw_input("\n****************\nEnter Name")
        try:
            if type(int(spy.name)) == int:
                temp = 0
        except:
            temp = len(spy.name)

    while spy.salutation != 'mr.' and spy.salutation != 'ms.':
        spy.salutation = raw_input("****************\nwhat should we call (mr.or ms.)")
    spy.name = spy.salutation + spy.name

    age = "not ok"
    while age == "not ok":
        spy.age = raw_input("****************\nplease enter age")
        try:
            if type(int(spy.age)) == int:
                age = "ok"
                spy.age = int(spy.age)
        except:
            print "\n!!!!!!!!!!!!!!!\nenter carefully\n!!!!!!!!!!!!!!!\n"
            age = "not ok"

    rating = "not ok"
    while rating == "not ok":
        spy.rating = raw_input(
            "****************\nplease enter spy rating (out of 10)")
        print "****************"
        try:
            if type(float(spy.rating)) == float:
                rating = "ok"
                spy.rating = float(spy.rating)
        except:
            print "\n!!!!!!!!!!!!!!!\nenter carefully\n!!!!!!!!!!!!!!!\n"
            rating = "not ok"

    spy.is_online = True

    return spy


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


def add_friend(spy_rating):
    friends_detail = spy_detail()
    if friends_detail.age > 12 and friends_detail.age < 50:
        if friends_detail.rating >= spy_rating:
            friends.append(friends_detail)
        else:
            print "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" \
                  "\nyour friend's rating must be greater than or equal to you" \
                  "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    else:
        print "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" \
              "\nyou'r friend is not eligible for a spy in this age" \
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    return len(friends)


def add_status(current_status_message):

    if current_status_message != None:
        print "\n*******************************\n your current status message is" \
              + " " + current_status_message + "\n*******************************"

    else:
        print "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" \
              "\n you don't have any status currently" \
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    temp = "not ok"
    while temp == "not ok":
        default = raw_input("\n***********************************************\n"
                            "do you want to select from the older status (y/n)"
                            "\n***********************************************")
        if default.upper() == 'N':
            temp = "ok"
            new_status_message = raw_input("\n*********************\nenter status message")
            print "*********************"
            if len(new_status_message) > 0:
                updated_status_message = new_status_message
                status_messages.append(updated_status_message)
                return updated_status_message

        elif default.upper() == 'Y':
            temp = "ok"
            item_position = 1
            for message in status_messages:
                print "\n" + str(item_position) + " " + message
                item_position =item_position + 1
            message_selection = int(raw_input("\nchoose a status"))
            if len(status_messages) >= message_selection:
                updated_status_message = status_messages[message_selection-1]
                return updated_status_message

        else:
            temp = "not ok"


def start_chat(spy_name, spy_age, spy_rating,):
    current_status_message = None
    if spy_age > 12 and spy_age < 50:
        print "\n\n\n**************************"
        print "welcome " + spy_name + "\n age: " + str(spy_age) + " \n rating: " + str(spy_rating)
        print "**************************"
        while 1:
            menu_choice = int(raw_input("\n**********what do you want to do?********** \n "
                                        "1. update a status \n 2.Add a friend \n "
                                        "3. send secret message to a friend \n"
                                        "4. read a secret message\n"
                                        "5. read chat history\n"
                                        "6. close application"
                                        "**********************************************\n"))
            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
                print "\n******************************"
                print "your status message is"
                print current_status_message
                print "**********************************"
            elif menu_choice == 2:
                no_of_friends = (add_friend(spy_rating))
                print "\n**********" + str(no_of_friends) + " friend/s added" + "**********"
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()
            elif menu_choice == 5:
                read_chat()
            elif menu_choice == 6:
                exit()
            else:
                print "\n!!!!!!!!!!!!!!!\nenter carefully\n!!!!!!!!!!!!!!!"
    else:
        print "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" \
              "\nyou are not eligible for a spy in this age" \
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

print("***************\n welcome!!!!.... \n***************")

proceed = "not ok"
while proceed == "not ok":
    proceed = raw_input("\nwant to proceed with default user (y/n)")
    if proceed.lower() == 'y':
        proceed = "ok"
        start_chat(spy.salutation + spy.name, spy.age, spy.rating)

    elif proceed.lower() == 'n':
        details = spy_detail()
        proceed = "ok"
        start_chat(details.name, details.age, details.rating,)
    else:
        print "\n!!!!!!!!!!!!!!!\nENTER CAREFULLY\n!!!!!!!!!!!!!!!"
        proceed = "not ok"
