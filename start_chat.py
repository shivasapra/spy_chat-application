from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
from read_chat import read_chat


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
