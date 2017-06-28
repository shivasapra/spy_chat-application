from steganography.steganography import Steganography
from spy_details import spy_name, spy_age, spy_salutation, spy_rating
from datetime import datetime

status_messages = ["die with memories not with dreams", "busy", "despacito", "Goooooogle!!!, i'm on my way"]

friends = []


def spy_detail():
    temp = 0
    while temp == 0:
        spy_name = raw_input("\nEnter Name\n----------------------")
        try:
            if type(int(spy_name)) == int:
                temp = 0
        except:
            temp = len(spy_name)

    salutation = ' '
    while salutation != 'mr.' and salutation != 'ms.':
        salutation = raw_input("\nwhat should we call (mr.or ms.)\n----------------------")
    spy_salutation = salutation
    spy_name = spy_salutation + spy_name

    age = "not ok"
    while age == "not ok":
        spy_age = raw_input("\nplease enter age\n----------------------")
        try:
            if type(int(spy_age)) == int:
                age = "ok"
        except:
            print("*************************************************")
            print("ENTER YOUR DETAILS CAREFULLY")
            print("*************************************************")
            age = "not ok"

    rating = "not ok"
    while rating == "not ok":
        spy_rating = raw_input(
            "\nplease enter spy rating (x.y out of 10 or an integer out of 100 )\n----------------------")
        try:
            if type(float(spy_rating)) == float:
                rating = "ok"
        except:
            print("*************************************************")
            print("ENTER YOUR DETAILS CAREFULLY")
            print("*************************************************")
            rating = "not ok"

    spy_is_online = True

    spy = {
        'name': spy_name,
        'age': spy_age,
        'rating': spy_rating,
    }

    return spy


def select_a_friend():
    if len(friends) > 0:
        print "here are your friends"
        for spy in friends:
            print "*****************************************************"
            print "% s aged % d with rating % f is online" % (spy['name'], int(spy['age']), float(spy['rating']))
            print "*****************************************************"
        item_number = 1
        for spy in friends:
            print '%d. %s' % (item_number, spy['name'])
            item_number = item_number + 1
        index = int(raw_input('choose option')) - 1
        return index
    else:
        print("you have no friends")


def add_friend():
    friends_detail = spy_detail()
    friends.append(friends_detail)
    return len(friends)


def add_status(current_status_message):

    if current_status_message != None:
        print "\n your current status message is" + current_status_message + "\n----------------------"
    else:
        print "\n you don't have any status currently\n----------------------"
    default = raw_input("\n \ndo you want to select from the older status (y/n)\n----------------------")

    if default.upper() == 'N':
        new_status_message = raw_input("enter status message\n----------------------")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            status_messages.append(updated_status_message)
            return updated_status_message

    elif default.upper() == 'Y':
        item_position = 1
        for message in status_messages:
            print str(item_position) + " " + message + "\n----------------------"
            item_position =item_position + 1
        message_selection = int(raw_input("choose a status\n----------------------"))
        if len(status_messages) >= message_selection:
            updated_status_message = status_messages[message_selection-1]
            return updated_status_message

    else:
        current_status_message=None
        add_status(current_status_message)


def start_chat(spy_name, spy_age, spy_rating,):
    current_status_message = None
    if spy_age > '18' and spy_age < '60':
        print "*****************************************************"
        print "\nwelcome " + spy_name + "\n age: " + spy_age + " \n rating: " + spy_rating
        print "*****************************************************"
        show_menu = True

        while show_menu:
            menu_choice = int(raw_input("\n**********what do you want to do?********** \n "
                                        "1. update a status \n 2.Add a friend \n "
                                        "5.exit application\n----------------------"))
            if menu_choice == 1:
                print "\nyou have to update the status\n----------------------"
                message = add_status(current_status_message)
                print "*****************************************************"
                print "\nyour status message is"
                print message + "\n----------------------"
                print "*****************************************************"
            elif menu_choice == 2:
                no_of_friends = str(add_friend())
                print no_of_friends + " friend/'s added"

            else:
                show_menu = False
    else:
        print "\nyou are not eligible for a spy in this age\n----------------------"

print("\n welcome!!!!.... \n----------------------")

proceed = " "
while proceed.lower() != 'y' and proceed.lower() != 'n':
    proceed = raw_input("want to proceed with default user (y/n)")
    if proceed.lower() == 'y':
        start_chat(spy_salutation + spy_name, spy_age, spy_rating)

    elif proceed.lower() == 'n':
        details = spy_detail()
        start_chat(details['name'], details['age'], details['rating'],)

    else:
        print "enter valid option\n----------------------"
