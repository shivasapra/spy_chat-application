from spy_details import status_messages


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
