from spy_details import spy, Spy
from spy_details import friends


# function to add a friend
def add_friend():
    new_friend = Spy(" ", " ", 0, 0.0)
    new_friend.name = raw_input("enter your friend's name")

    new_friend.salutation = raw_input("are they mr. or ms. or any other? : ")

    new_friend.name = new_friend.salutation + new_friend.name

    new_friend.age = raw_input("enter age")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and 12 < new_friend.age < 50 and new_friend.rating >= spy.rating:
        friends.append(new_friend)

    else:
        print "sorry Invalid entry,We can't add your friend"

    return len(friends)
