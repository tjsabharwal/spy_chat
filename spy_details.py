#File to be imported to fetch default user and arious other details.

from datetime import datetime

class Spy:

    def __init__(self,name,age,salutation,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []  #It stores the chat, so that to keep a track on the what are the messages exchanged.

old = 0
friends = [] #List to store the n number of friends
spy = Spy('bond', 24, 'Mr', 2.4)  #Default user

class chat:
    def __init__(self, msg,sent_by_me):  #Functio to initalize and store the incoming data to the local variables.
        self.message = msg
        self.datetime = datetime.now()
        self.sent_by_me = sent_by_me