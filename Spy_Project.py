from spy_details import Spy, old, friends, spy, chat
from steganography.steganography import Steganography
from datetime import datetime


Status_messages = ["Available", "Can't talk right now!", "Driving", "Busy"]

user = raw_input("Do you want to continue as default user i.e [%s. %s] (y/n)? " % (spy.salutation, spy.name))

if user.lower() == "y":
    print "Authentication completed."
    print 'Welcome %s. %s, your age is %d with rating %.2f' % (spy.salutation, spy.name, spy.age, spy.rating)
    old = 1
elif user.lower() == "n":
    new_spy = Spy('', '', 0, 0.0)
    new_spy.name = raw_input("Enter your name: ")
    new_spy.salutation = raw_input("Enter salutation: ")
    new_spy.age = int(raw_input ("Enter your age: "))
    new_spy.rating = float(raw_input("Enter your rating: "))
    count = 0
    for i in new_spy.name:
        if not i.isalpha():
            count = count + 1
    if count != 0:
        print "\nWARNING: Invalid name entented"
        exit()
    count = 0
    for i in new_spy.salutation:
        if not i.isalpha():
            count = count + 1
    if count != 0:
        print "\nWARNING: Invalid saluation entented"
        exit()
    if new_spy.name == "":
        print "Name cannot be left empty."
        exit()
    elif new_spy.age >=50 or new_spy.age <= 12:
        print "Your age is not eligible to be a spy."
        exit()
    elif new_spy.rating < 0:
        print "Invalid spy rating."
        exit()
    elif new_spy.rating > 5:
        print "Invalid spy rating."
        exit()
    else:
        print "Authentication completed."
        print 'Welcome %s. %s, your age is %d with rating %.2f' % (new_spy.salutation, new_spy.name, new_spy.age, new_spy.rating)
        if 2.5 >= new_spy.rating >= 0:
            print "You are an average spy."
        elif 4.0 >= new_spy.rating > 2.5:
            print "You are a good spy."
        elif 5 >= new_spy.rating > 4.0:
            print "You are a brilliant spy."
        old = 0
else:
    print "Wrong input."
    exit()

def add_status():
    index = 0
    for i in Status_messages:
        index = index + 1
        print index, i
    option = raw_input("Do you want to select from older statuses (y/n)? ")
    index = index -1
    if option.upper() == "Y":
        chose = int(raw_input("Enter you choice: "))
        chose = chose - 1
        if index >= chose >= 0:
            current_status_message = Status_messages[chose]
            print "New status = %s " % (current_status_message)
        else:
            print 'Wrong input.'
    elif option.upper() == "N":
        new_status = raw_input("Enter new status: ")
        if new_status != "" and new_status.isspace() == False:
            Status_messages.append(new_status)
            current_status_message = new_status
            print "New status = %s " % (current_status_message)
        else:
            print "Type a status to add."
    else:
        print 'Wrong input.'

def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Enter friend's name: ")
    new_friend.salutation = raw_input("Enter friend's salutation: ")
    new_friend.age = int(raw_input("Enter friend's age: "))
    new_friend.rating = float(raw_input("Enter friend's rating: "))
    count = 0
    for i in new_friend.name:
        if not i.isalpha():
            count = count + 1
    if count != 0:
        print "\nWARNING: Invalid name entented"
    count1 = 0
    for i in new_friend.salutation:
        if not i.isalpha():
            count1 = count1 + 1
    if count1 != 0:
        print "\nWARNING: Invalid saluation entented"
    if count == 0 and count1 == 0:
        if old == 1:
            if new_friend.name != "" and 12 < new_friend.age < 50 and new_friend.rating >= spy.rating and new_friend.rating <= 5:
                friends.append(new_friend)
                print "New friend added."
            else:
                if new_friend.rating < 0 or new_friend.rating > 5:
                    print "Friend's rating entered is not eligible"
                elif new_friend.rating < spy.rating :
                    print "Friend's rating is less than the spy rating."
                elif new_friend.age <= 12 or new_friend.age >= 50:
                    print "Friend's age is not eligible."
                elif new_friend.name == "":
                    print "Friend's name cannot be left empty."
        elif old == 0:
            if new_friend.name != " " and 12 < new_friend.age < 50 and new_friend.rating >= spy.rating and new_friend.rating <= 5 :
                friends.append(new_friend)
                print "New friend added."
            else:
                if new_friend.name == "":
                    print "Friend's name cannot be left empty."
                elif new_friend.age <= 12 or new_friend.age >= 50:
                    print "Friend's age is not eligible."
                elif new_friend.rating < new_spy.rating:
                    print "Friend's rating is less than the spy rating."
    return len(friends)

def select_a_friend(task):
    index = 0
    for i in friends:
        index = index + 1
        print '%d. %s. %s aged %d with rating %.2f is online' % (index, i.salutation, i.name, i.age, i.rating)
    if task == 0:
        select = int(raw_input("Select one of the friends to send message: "))
    if task == 1:
        select = int(raw_input("Select friend from whom you want to read message: "))
    if task == 2: #this
        select = int(raw_input("Select friend whose chat you want to read: "))
    if index >= select >0:
        select = select -1
        return select
    else:
        return -1

def send_a_message():
    send = 0
    friend_selected = select_a_friend(send)
    if friend_selected != -1:
        output_path = raw_input("save_as: ")
        image = raw_input("Enter the name of the image to which you want to encrypt the message: ")
        secret_message = raw_input("Enter the secret message you want to encrypt: ")
        if image != "" and secret_message != "":
            Steganography.encode(image,output_path,secret_message)
            print "Message sent"
            new_chat = chat(secret_message, True)
            friends[friend_selected].chats.append(new_chat)
            #here this is while sending, you ned to this read also
            print friends[friend_selected].chats
        if image == "":
            print "You did not enter the Image name\nMessage was not sent"
        elif secret_message == "":
            print "You did not enter the message\nMessage was not sent"
    else:
        print "Friend not selected"

def read_a_message():
    read = 1
    friend_selected = select_a_friend(read)
    secret_message = ""
    if friend_selected != -1:
        output_path = raw_input("Enter the image name: ")
        secret_message = Steganography.decode(output_path)
        if secret_message != "":
            print secret_message
            new_chat = chat(secret_message, False)
            friends[friend_selected].chats.append(new_chat)
        else:
            print "There is no sercret message."
    else:
        print "Friend not selected"
        #hey you are not appending the message to frineds chat object

def read_chat():
    r_chat = 2
    person = select_a_friend(r_chat)
    if person != -1:
        for chat in friends[person].chats:
            if chat.sent_by_me:
                print '[%s] %s: %s' % (chat.datetime.strftime("%d %B %Y"), 'You said:', chat.message)
            else:
                print '[%s] %s said: %s' % (chat.datetime.strftime("%d %B %Y"), friends[person].name, chat.message)
    else:
        print "Friend not selected"
def begin():
    while True:
        select = int(raw_input("\nChoose an option:\n\n1) Add a status update\n2) Add a friend\n3) Send a secret message\n4) Read a secret message\n5)"
                               " Read chats from a user\n6) Close application\n\nYour selection = "))
        if select == 1:
            add_status()

        elif select == 2:
            total_friends = add_friend()
            print "total friends = %d" % (total_friends)

        elif select == 3:
            send_a_message()
        elif select == 4:
            read_a_message()
        elif select == 5:
            read_chat()
        elif select == 6:
            print "Closing Application..."
            exit()
        else:
            print "You made a wrong choice."
begin()