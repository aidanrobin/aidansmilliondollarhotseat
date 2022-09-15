from kivy.app import App                                    #
from kivy.lang import Builder                               #
from kivy.uix.screenmanager import ScreenManager, Screen    #
from kivy.properties import ObjectProperty                  #
from kivy.uix.popup import Popup                            #import the following kivy modules
from kivy.uix.label import Label                            #
from userdetailsdatabase import DataBase                    #
from subprocess import call                                 #import the call function from the subprocess module, which helps call other python files



class CreateAccountWindow(Screen):  #This class creates an object constructor for the Create Account Window
    username = ObjectProperty(None) #
    email = ObjectProperty(None)    #username, email and password are initialised as Object properties of the class, and are stated as None as they have no value
    password = ObjectProperty(None) #

    def submit(self):               #This function refers to what happens when the user presses the submit button on the creating account page
        if self.username.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:   #If the username and email are not empty strings, the email features the @ symbol once, and the "." appears more than once...
            if self.password != "":                                                                 #if the user's password is not an empty string
                UserDetails.add_user(self.email.text, self.password.text, self.username.text)       #add the user's details to the database

                self.reset()                                                                        #reset the page

                ScreenManagers.current = "login"                                                    #return to the login page
            else:
                invalidForm()                                                                       #if the password is an empty string, call the invalidForm function
        else:
            invalidForm()                                                                           #if the username or email is empty, or the count of "@" is not 1, or the "." count is 0, call the InvalidForm function

    def login(self):                        #this determines what happens if the user presses the "Already have a Login" on the create account page
        self.reset()                        #The home screen is reset
        ScreenManagers.current = "login"    #The user is redirected to the login page.

    def reset(self):             # This defines what happens if the user presses another page: if any variables are not empty, they need to be reset
        self.email.text = ""     #
        self.password.text = ""  # resets the email, username and password texts to empty strings.
        self.username.text = ""  #

class LoginWindow(Screen):           # Defines a blueprint of what happens when the LoginWindow is executed
    email = ObjectProperty(None)     #
    password = ObjectProperty(None)  # password, email and created are initialised as Object properties of the class, and are stated as None as they have no value

    def loginBtn(self):                                                 # defines what happens if the login button is pressed
        if UserDetails.validate(self.email.text, self.password.text):   # if the email and password are valid
            MainWindow.current = self.email.text                        # set the current elemenet of the MainWindow as the email
            self.reset()                                                # call the reset function to reset all variables
            ScreenManagers.current = "main"                             # redirect the user to the "main" page
        else:
            invalidLogin()                                              # If the user details are invalid, call the Invalid Login function

    def createBtn(self):                            #This defines what happens if the Create Account button is pressed
        self.reset()                                #call the self.reset function, which resets the values of the email, username and password to empty strings
        ScreenManagers.current = "create"           #Make the current page the "create" page.

    def reset(self):                                #This function defines what happens if the user resets their password
        self.email.text = ""                        #Email becomes an empty string
        self.password.text = ""                     #Password becomes an empty string


class MainWindow(Screen):
    accountname = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def GameButton(self):                       #This defines what happens if the Game Button is chosen
        ScreenManagers.current = "IntroGame"    #Redirect the user to the Intro Game page


    def logOut(self):                           #This defines what happens if the LogOut button is chosen
        ScreenManagers.current = "login"        #Redirects the user to the Login Page

class ChatbotWindow(Screen):                    #Defines a blueprint of what happens if the Chatbot Window is called
    pass                                        #pass: nothing is called as the code for this is in the my.kv file

class GameWindow(Screen):                       #Defines a blueprint of what happens if the Game Window is called
    pass                                        #pass: nothing is called as the code for this is in the my.kv file

class IntroGameWindow(Screen):                  #Defines a blueprint of what happens if the IntroGame Window is called
    pass                                        #pass: nothing is called as the code for this is in the my.kv file

class InstructionsWindow(Screen):               #Defines a blueprint of what happens if the Instructions Window is called
    def GameRun(self):                          #This function declares what happens if the "Play Game" button is pressed in the instructions window
        call(["python", "game.py"])             #The "game.py" file is called, and executed.

class WindowManager(ScreenManager):             #Defines a blueprint of what the WindowManager is required to do
    pass                                        #pass: nothing is called as the code for this is in the my.kv file



def invalidLogin():                                                     #If the user login is invalid
    pop = Popup(title='Invalid Login',                                  #Add a popup that states that the user details were invalid
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))              #ensure the label has no hint size
    pop.open()                                                          #open the popup


def invalidForm():                                                                          #This function defines what heppens if the user does not follow the requirements of the create account form
    pop = Popup(title='Invalid Form',                                                       #Add a popup that states that the account form was invalid
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()                                                                              #open the popup

kv = Builder.load_file("my.kv")             #creates a Parser for parsing/compiling a kv file

ScreenManagers = WindowManager()            #Creates a WindowManager widget, responsible for managing multiple screens for the application
UserDetails = DataBase("users.txt")         #Call the UserDetails the user.txt file from the database

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),               #Create a list of each Kivy screen used in the app, alongside its name
           MainWindow(name="main"),                                                     #
           GameWindow(name="game"), IntroGameWindow(name="IntroGame"),                  #
           InstructionsWindow(name="instructions"), ChatbotWindow(name="chatbot")]      #

for screen in screens:                  #for each screen in the screens list
    ScreenManagers.add_widget(screen)   #add each screen to the WindowManager()

ScreenManagers.current = "login"        #set the current screen as the login page


class MyMainApp(App):                   #creates a class for running the app
    def build(self):                    #this function builds the app's Screens
        return ScreenManagers           #returns the ScreenManagers variable, featuring all of the screens of the app


if __name__ == "__main__": #if the code was run directly, and not imported...
    MyMainApp().run()      #run the Main App
