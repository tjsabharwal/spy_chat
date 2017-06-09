import spy_details
friend_name = [ ]
friend_age = [ ]
friend_rating = [ ]
spy = {
    'name': " ",
    'salutation' : " ",
    'spy_rating' : 0.0,
    'spy_age' : 0
}
online_status = False
friend = {
    'name': '',
    'salutation': '',
    'age': 0,
    'rating': 0.0
}
friends = []
def add_friend():
    friend['name'] = raw_input("Enter friend's name: ")
    friend['age'] = int(raw_input("Enter friend's age: "))
    friend['rating'] = float(raw_input("Enter friend's rating: "))
    if spy_details.old == 1:
        if friend_name != " " and friend_age > 12 and friend_age <50 and friend_rating >= spy_details.spy['rating']:
            friends.append(friend)
            print "New friend added."
        else:
            if friend_rating < spy_details.spy['rating']:
                print "Friend's rating is less than the spy rating."
            elif friend_age <= 12 or friend_age >= 50:
                print "Friend's age is not eligible."
            elif friend_name == "":
                print "Friend's name cannot be left empty."
            print "Friend not added."
    elif spy_details.old == 0:
        if friend_name != "" and friend_age > 12 and friend_rating >= spy['rating']:
            friends.append(friend)
            print "New friend added."
        else :
            if friend_rating < spy['rating']:
                print "Friend's rating is less than the spy rating."
            elif friend_age > 12:
                print "Friend's age is less than or equal to 12."
            elif friend_name == "":
                print "Friend's name cannot be left empty."
            print "Friend not added."

def select_a_friend():
    index=1
    for i in friend['name']:
        print index , " " , i
    choice = raw_input("Select your friend you want to communicate with: ")
    choice = choice-1
    return (choice)

def send_a_message():
    friend = select_a_friend()
    image = raw_input("Enter the name of the image to which you want to encrypt the message")
    secret_message = raw_input("Enter the secret message you want to encrypt")

def get_info():
    if spy_details.old == 1:
        count = 0
        for i in spy_details.spy['name']:
            if not i.isalpha():
                count = count + 1
        if count != 0:
            print "\nWARNING: Invalid name enterted"
            exit()
        else:
            if 12 < spy_details.spy['age'] < 50:
                print "\nWelcome %s. %s,\nSpy age : %d\nSpy rating : %.2f" % (spy_details.spy['salutation'], spy_details.spy['name'], spy_details.spy['age'], spy_details.spy['rating'])
                if spy_details.spy['rating'] >= 4.0:
                    print "You are a brilliant spy."
                elif spy_details.spy['rating'] >= 2.0 and spy_details.spy['rating'] < 3.0:
                    print "You are an average spy."
                elif spy_details.spy['rating'] >= 3.0 and spy_details.spy['rating'] < 4.0:
                    print "You are a good spy."
                else:
                    print "You are not a good spy."

            else:
                print "WARNING: Your age does not fit to be a spy."
                exit()
    else:
        count = 0
        spy['name'] = raw_input("Enter spy name: ")
        for i in spy['name']:
            if not i.isalpha():
                count = count + 1
        if count != 0:
            print "\nWARNING: Invalid name enterted"
            exit()
        else:
            spy['salutation'] = raw_input("Enter spy salutation : ")
            spy['age'] = int(raw_input("Enter spy age : "))
            if 12 < spy['age'] < 50:
                spy_rating = float(raw_input("Enter spy rating : "))
                print "\n\nSpy Details\n\nSpy name : %s %s\nSpy age : %d\nSpy rating : %.2f" % (
                spy['salutation'], spy['name'], spy['age'], spy['rating'])
                if spy['rating'] >= 4.0:
                    print "\nYou are a brilliant spy."
                elif spy['rating'] >= 2.0 and spy['rating'] < 3.0:
                    print "\nYou are an average spy."
                elif spy['rating'] >= 3.0 and spy['rating'] < 4.0:
                    print "\nYou are a good spy."
                else:
                    print "You are not a good spy."

            else:
                print "WARNING: Your age does not fit to be a spy."
                exit()
def create_user():
    index = 0
    old_statuses = ["Available","Busy","Can't reply right now.","Driving"]
    current_status_message = "Available"
    choice = raw_input("Do you want to create a new user (y/n)")
    if choice.upper() == "Y":
        get_info()
    if choice.upper() == "N":
        spy_details.old = 1
        get_info()
    while True:
        select = int(raw_input("\nChoose an option:\n\n1) Add a status update\n2) Add a friend\n3) Send a secret message\n4) Read a secret message\n5) Read chats from a user\n6) Close application\n\nYour selection = "))
        if select == 1:
            print "Current status = " + current_status_message
            option = raw_input("Do you want to select from older statuses (y/n)?")
            if option.upper() == "Y":
                for i in old_statuses:
                    index = index + 1
                    print "%d. %s" %(index,i)
                chose = int(raw_input("Enter you choice: "))
                current_status_message = old_statuses[chose-1]
            else:
                new_status = raw_input("Enter new status: ")
                old_statuses.append(new_status)
                current_status_message=new_status
            print "New status = " + current_status_message
        elif select == 2:
            chose = raw_input("Do you want to add a friend (y/n)?")
            if chose.upper() == "Y":
                add_friend()
            else:
                continue
            total_friends =0
            for i in friend['name']:
                print i
                total_friends = total_friends + 1
            print "Total number of friends user has = %d" %(total_friends)
        elif select == 3:
            send_a_message()
        elif select == 6:
            exit()
create_user()