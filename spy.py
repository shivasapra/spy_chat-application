# importing files
from spy_details import spy
from start_chat import start_chat
from spy_detail import spy_detail

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
