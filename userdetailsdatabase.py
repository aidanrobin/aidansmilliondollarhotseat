import datetime                     #import the date time module


class DataBase: #Creates an object constructor for the Data Base
    def __init__(self, filename): #A function that initialises the attributes of the DataBase class
        self.filename = filename  #declares the self.filename variable as filename
        self.users = None         #declares the self.users variable as None (There is nothing inside it)
        self.file = None          #declares the self.file variable as None (as there is nothing inside it)
        self.load()               #calls the self.load function

    def load(self):                                                     #a function that loads the user details from the text file.
        self.file = open(self.filename, "r")                            #open the users file, for reading purposes
        self.users = {}                                                 #create an empty dictionary for the users

        for line in self.file:                                          #for each line in the file
            email, password, name, created = line.strip().split(";")    #split the email, password, name and date created by a ";"
            self.users[email] = (password, name, created)               #match each user email with the password, name of user and the date created.

        self.file.close()                                               #close the file

    def get_user(self, email):                                          #this function demonstrates what happens if the user wants to "get" their email
        if email in self.users:                                         #if the email exists in the user dictionary
            return self.users[email]                                    #return the users email
        else:
            return -1                                                   #else return that the user does not exist

    def add_user(self, email, password, name):                                                  #This function declares what happens if the user chooses to create a new account
        if email.strip() not in self.users:                                                     #if the email is not in the user list...
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())   #if the stripped email does not
            self.save()                                                                         #calls the self.save function
            return 1                                                                            #Return 1: The email was created
        else:
            print("Email exists already")           # If the email is in the user dictionary, print that it already exists
            return -1                               # return -1 to show the occurence was False

    def validate(self, email, password):                #this function shows whathappens when the user validates their email and password (i.e. the app confirms if their details are legitimate)
        if self.get_user(email) != -1:                  #if the user email is not a false occurence (i.e. it exists)
            return self.users[email][0] == password     #Return the password to the email that the user has entered
        else:
            return False                                #If the user email is a false occurence, return False to represent this

    def save(self):                                         #This function defines what happens once the user creates their account and submits it
        with open(self.filename, "w") as fileToOpen:        #Open the user database to write to is
            for user in self.users:                         #For the user in the user dictionary
                fileToOpen.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")    #Write the user's details to the file, splitting each aspect with a ";", and adding a newline at the end

    @staticmethod
    def get_date():                                         #This function defines what happens if the
        return str(datetime.datetime.now()).split(" ")[0]   #return the time of the login