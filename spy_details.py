from datetime import datetime

class Spy:

    def __init__(self,name,age,salutation,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []

old = 0
friends = []
spy = Spy('bond', 24, 'Mr', 2.4)

class chat:
    def __init__(self, msg,sent_by_me):
        self.message = msg
        self.datetime = datetime.now()
        self.sent_by_me = sent_by_me