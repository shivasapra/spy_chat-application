from spy_details import Spy


# function defined for taking details from spy
def spy_detail():
    spy = Spy(" ", " ", 0, 0.0)
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
