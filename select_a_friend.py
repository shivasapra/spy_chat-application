from spy_details import friends


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
