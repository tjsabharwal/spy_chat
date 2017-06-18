from spy_details import Spy, old, friends, spy, chat
from steganography.steganography import Steganography
import datetime
import termcolor

Status_messages = ["Available", "Can't talk right now!", "Driving", "Busy"]  # Default statuses
Special_words = ["SOS","help","save me"]

total_reads = 0
avg = 0

user = raw_input("Do you want to continue as default user i.e [%s. %s] (y/n)? " % (spy.salutation, spy.name))
if user.lower() == "y":
    print "Authentication completed."
    print 'Welcome %s. %s, your age is %d with rating %.2f' % (spy.salutation, spy.name, spy.age, spy.rating)
    old = 1 #Further used to check the defualt user or new user.
elif user.lower() == "n":
    new_spy = Spy('', '', 0, 0.0) #Creating object for class 'Spy'
    new_spy.name = raw_input("Enter your name: ")
    new_spy.salutation = raw_input("Enter salutation: ")
    new_spy.age = int(raw_input ("Enter your age: "))
    new_spy.rating = float(raw_input("Enter your rating: "))
    count = 0
    for i in new_spy.name: #Checking for valid name input.
        if not i.isalpha():
            count = count + 1
    if count != 0:
        print "\nWARNING: Invalid name entented"
        exit()
    count = 0
    for i in new_spy.salutation: #Checking for valid salutation input.
        if not i.isalpha():
            count = count + 1
    if count != 0:
        print "\nWARNING: Invalid saluation entented"
        exit()
    if new_spy.name == "": #Handling the corner case for empty name.
        print "Name cannot be left empty."
        exit()
    elif new_spy.age >=50 or new_spy.age <= 12: #Checking age eligibility.
        print "Your age is not eligible to be a spy."
        exit()
    elif new_spy.rating < 0: #checking valid rating input.
        print "Invalid spy rating."
        exit()
    elif new_spy.rating > 5: #checking valid rating input.
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
    print "Wrong input." #checking if only 'y' or 'n' is pressed.
    exit()

def add_status(): #Function to add a status.
    index = 0
    for i in Status_messages: #Loop to print the list of available statuses with us.
        index = index + 1
        print index, i
    option = raw_input("Do you want to select from older statuses (y/n)? ")
    index = index -1
    if option.upper() == "Y": #if user wants to select from the available statuses.
        chose = int(raw_input("Enter you choice: "))
        chose = chose - 1
        if index >= chose >= 0:
            current_status_message = Status_messages[chose] #selected status will be changed to current or new status.
            print "New status = %s " % (current_status_message)
        else:
            print 'Wrong input.' #checking for correct index input of available statuses.
    elif option.upper() == "N": #if user wants to enter new status.
        new_status = raw_input("Enter new status: ")
        if new_status != "" and new_status.isspace() == False: #Checking for correct input of the new status.
            Status_messages.append(new_status)
            current_status_message = new_status
            print "New status = %s " % (current_status_message)
        else:
            print "Type a status to add." #if new status is left empty.
    else:
        print 'Wrong input.' #checking if only 'y' or 'n' is pressed.

def add_friend(): #Function to add a friend.

    new_friend = Spy('','',0,0.0) #Creating object for class 'Spy'

    new_friend.name = raw_input("Enter friend's name: ") #taking input.
    new_friend.salutation = raw_input("Enter friend's salutation: ")
    new_friend.age = int(raw_input("Enter friend's age: "))
    new_friend.rating = float(raw_input("Enter friend's rating: "))
    count = 0
    for i in new_friend.name: #checking valid name or not.
        if not i.isalpha():
            count = count + 1
    if count != 0:
        print "\nWARNING: Invalid name entented"
    count1 = 0
    for i in new_friend.salutation: #checking valid salutation or not.
        if not i.isalpha():
            count1 = count1 + 1
    if count1 != 0:
        print "\nWARNING: Invalid saluation entented"
    if count == 0 and count1 == 0:
        if old == 1:
            if new_friend.name != "" and 12 < new_friend.age < 50 and new_friend.rating >= spy.rating and new_friend.rating <= 5:
                friends.append(new_friend)
                print "New friend added."
            else: #checking all corner cases.
                if new_friend.rating < 0 or new_friend.rating > 5:
                    print "Friend's rating entered is not eligible"
                elif new_friend.rating < spy.rating :
                    print "Friend's rating is less than the spy rating."
                elif new_friend.age <= 12 or new_friend.age >= 50:
                    print "Friend's age is not eligible."
                elif new_friend.name == "":
                    print "Friend's name cannot be left empty."
        elif old == 0: #if user selects for the new user, then we check the rating with the new user's rating with friend's rating.
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
    return len(friends) #For number of friends.

def select_a_friend(task): #task is for printing appropiate msg depending upon which function is calling it.
    index = 0
    for i in friends:
        index = index + 1
        print '%d. %s. %s aged %d with rating %.2f is online' % (index, i.salutation, i.name, i.age, i.rating)
    if task == 0:
        select = int(raw_input("Select one of the friends to send message: "))
    elif task == 1:
        select = int(raw_input("Select friend from whom you want to read message: "))
    elif task == 2:
        select = int(raw_input("Select friend whose chat you want to read: "))
    if index >= select >0:
        select = select -1
        return select
    else:
        return -1

def send_a_message():
    send = 0
    friend_selected = select_a_friend(send) #'send' to print specific message to select a friend
    if friend_selected != -1:
        output_path = raw_input("save_as: ")
        image = raw_input("Enter the name of the image to which you want to encrypt the message: ")
        secret_message = raw_input("Enter the secret message you want to encrypt: ")
        if image != "" and secret_message != "":
            Steganography.encode(image,output_path,secret_message) #encode method is used to encrypt the msg with the file.
            print "Message sent"
            new_chat = chat(secret_message, True)
            friends[friend_selected].chats.append(new_chat)
        if image == "": #checking all corner cases.
            print "You did not enter the Image name\nMessage was not sent"
        elif secret_message == "":
            print "You did not enter the message\nMessage was not sent"
    else:
        print "Friend not selected" #Handling corner case for wrong input for selection of a friend.

def read_a_message():
    read = 1

    global avg
    global total_reads

    friend_selected = select_a_friend(read) #'read' to print specific message to select a friend
    if friend_selected != -1:
        output_path = raw_input("Enter the image name: ")
        secret_message = Steganography.decode(output_path) #decode method is used to decrypt the msg from the file.
        if secret_message != "":
            print secret_message
            new_chat = chat(secret_message, False) #saving the secret essage to the chats.
            total_words = avg * total_reads + len(secret_message.split())
            total_reads = total_reads +1
            friends[friend_selected].chats.append(new_chat)
            avg = total_words/total_reads #checking average words spoken by a spy.
            print "Average words spoken by a spy = %d" % (avg)
        else:
            print "There is no sercret message." #Handling corner case for no secret message.
    else:
        print "Friend not selected" #Handling corner case for wrong input for selection of a friend.

def read_chat(): #Function to print the chat history
    r_chat = 2
    flag = 1
    friend_message = ""
    person = select_a_friend(r_chat) #r_chat to print specific message to select a friend
    if person != -1:
            for chatt in friends[person].chats:
                friend_message = chatt.message
                if chatt.message != "":
                    time = termcolor.colored(chatt.datetime.strftime("%d-%B-%Y"),'blue')
                    spyname = termcolor.colored(friends[person].name, 'red')
                    if chatt.sent_by_me:
                        print time+' You said: ',chatt.message
                        flag = 0
                    else:
                        if flag == 1:
                            print time + ' ' + spyname + ' Said: ', chatt.message
                    if len(friend_message.split()) > 100: #if spy speaks more than 100 words, he'll no longer be a spy.
                        friends.__delitem__(person)
                        print "Friend deleted as he spoke more than 100 words, [ %d ] words." %(len(friend_message.split()))
                    index= 0
                    flag = 0
                    while True: #Loop to check special words in chat history
                        if Special_words[index] in friend_message.split():
                            index = index + 1
                            flag = 1
                            if flag == 1 or index > len(friend_message.split()):
                                break
                        if flag == 0:
                            break
                    if flag == 1:
                        print "There is Special Word in the chat."
                else:
                    print "Chat is empty"
    else:
        print "Friend not selected" #Handling corner case for wrong input for selection of a friend.
def begin(): #this is the parent function which calls each and every function in it.
    while True:
        #taking input from user from the list of options.
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
        else: #checking for valid input by the user.
            print "You made a wrong choice."
begin()