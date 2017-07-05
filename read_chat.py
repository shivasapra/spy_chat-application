from datetime import datetime
from spy_details import spy
from select_a_friend import select_a_friend
from spy_details import friends


# function defined to read chat
def read_chat():
    read_for = select_a_friend()
    from colorama import init, Fore
    # initializing
    for chat in friends[read_for].chat:
        if chat.sent_by_me:
            print '[%s] [%s], %s %s    :   %s' % (chat.time.strftime("%d %B %Y"),
                                                  Fore.BLUE + chat.time.strftime("%H:%M:%S"),
                                                  Fore.RED + spy.name,  Fore.BLACK + "said" ,chat.message)
        else:
            print '[%s] [%s], %s %s %s : %s' % (chat.time.strftime("%d %B %Y"), Fore.BLUE +
                                                chat.time.strftime("%H:%M:%S"), Fore.RED + friends[read_for].salutation,
                                                Fore.RED + friends[read_for].name,Fore.Black + "Recieved",chat.message)
