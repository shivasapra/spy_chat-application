from datetime import datetime


class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chat = []
        self.current_satus_message = None

spy = Spy("holmes", "Mr.", 24, 6.7)

class ChatMessage :
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now
        self.sent_by_me = sent_by_me

class maintain:
    temp = 1
    get = 0
    def __init__(self,text):
        self.text = text
        maintain.get = (maintain.get +len(self.text.split()))/maintain.temp
        maintain.temp += 1

# list of status messages
status_messages = ["die with memories not with dreams", "busy", "despacito", "Goooooogle!!!, i'm on my way"]

# list of friend
friends = []
