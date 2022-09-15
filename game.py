from tkinter import *                   #imports everything from the Tkinter module
import time                             #imports the time module
from tkinter import messagebox as mb    #import the messagebox function from the tkinter module, declaring it as mb
from tkinter import simpledialog        #import the simpledialog function from the tkinter module
import json                             #import the json module (so the json file containing the questions can be added to the code)
import webbrowser                       #import the webbrowser module so the game can open the help website
import random                           #import the random module. This is done so questions can be randomised for each user to be asked.

class Quiz: #Creates an object constructor for the game
    def __init__(self): #A function that initialises the attributes of the Quiz class
        self.DataSize = 24                                          #sets the maximum amount of Questions a user can be Asked
        self.QuestionNumber = random.randint(0, self.DataSize)      #this variable randomizes a number between 0 and 24, where that number is the Question that will be Asked
        self.AskedList = []                                         #a List that stores each Asked Question
        self.AskedList.append(self.QuestionNumber)                  #Appends the random Question to a List
        print(self.AskedList)
        self.Display_Title()                                        #calls and initialises the Display Title function
        self.Display_Question()                                     #calls and initialises the Display Question function
        self.Opt_Selected = IntVar()                                #this variable holds an integer with the default value 0 (i.e. the user has not selected an answer yet)
        self.Opts = self.Radio_Buttons()                            #declare the user's options to be shown in the format of radio buttons
        self.Display_Options()                                      #calls and initialises the Display Option function
        self.Buttons()                                              #calls and initialises the Buttons function
        self.Correct = 0                                            #sets the amount of questions the user has answered correct as 0
        self.Counter = 1                                            #Sets the Active Question's worth at $1

        self.Answer = simpledialog.askstring("Name", "What is your first name?", parent=gui)                        #sets a popup that asks the user for their name
        while self.Answer is None or self.Answer == "":                                                             #while the input is an empty string or the user presses the "cancel Button"
            mb.showinfo("Error", "You must have a name")                                                            #prints an error message that states for the user to have a name
            self.Answer = simpledialog.askstring("Name", "What is your first name?", parent=gui)                    #keeps asking user to input a name until it satisfies commands of while loop (not an empty string)

        WelcomeLabel = Label(gui, text="Welcome {}!".format(self.Answer), fg="white", font=("ariel", 30, "bold"))   #a label that prints a welcome message to the user
        WelcomeLabel.place(x=60, y=60)                                                                              #places the label on the GUI using the x and y position
        
        mb.showinfo("Count", "You are currently playing for ${}".format(self.Counter))                              #popup message to show how much the Question is worth

        self.MoneyAtStake()                                                                                         #Calls the MoneyAtStake function
        self.MoneyBoard()                                                                                           #Calls the MoneyBoard functoin

    def Display_Result(self):
        FinalInitialStatement = "Congratulations! You have Answered every Question and have won the game!\n You have won ${}".format(int(round(self.Counter))) #Declare an alert that tells the user how much money they have won. The format is int(round(self.Counter/2)) as the counter multiplies by 2 before this command is executed.
        mb.showinfo("Result", f"{FinalInitialStatement}")   #A popup message that prints the string above.
        mb.showinfo("Message", "Thanks for playing!")       #A popup that thanks the users for playing the game
        gui.destroy()                                       #destroys the GUI

    def QuitApp(self): #This function defines what will happen if the user chooses to quit the app (Choose the quit button)
        QuitMessage = mb.askquestion("Exit the Application", 'Are you sure?', icon='warning')         #Ask the user if they want to quit the program (use a warning sign as an icon)
        if QuitMessage == 'yes':                                                                      #If they choose "yes"
            gui.destroy()                                                                             #Destroy the GUI application (choose for it to close)
        else:
            mb.showinfo("Return", "You will return to the current screen")                            #else print a popup that tells the user that they will return to the current screen

    def CheckAnswer(self, QuestionNumber): #This function checks if the user has answered the question correctly
        if self.Opt_Selected.get() == Answer[self.QuestionNumber]:      #If the option that the user selects is correct...
            mb.showinfo("Result", "You were Correct!!")                 #Print a pop-up that tells the user they were correct
            return True                                                 #Return that the user got the question correct
        else:
            Correct_Answer = Answer[self.QuestionNumber]                                            #Declares the position of the correct answer for the respective question.
            Correct_choice = Options[self.QuestionNumber][Correct_Answer -1]                        #Declares the correct choice as the position of the correct answer within the question's options
            mb.showinfo("Result", "Sorry, the Correct Answer was {}.".format(Correct_choice))       #A popup to inform the user of the correct answer.
            mb.showinfo("Alert", "You have incorrectly Answered this Question.\n You have lost. ")  #A popup to inform the user that they have answered the question wrong and lost
            mb.showinfo("Return", "Returning to the home screen. ")                                 #A popup that shows the user returning to the home screen
            gui.destroy()                                                                           #Destroys/Ends the GUI

    def OpenWeb(self): #if the user presses the help button (Open the Help Page)
        webbrowser.open('https://aidanrobinson264.wixsite.com/AIEVC', new=1) #opens the help page. New = 1 references that the help page will open in a new window.

    def NextButton(self): #Declares what happens if the user presses the next button
        if self.CheckAnswer(self.QuestionNumber):                                                                       #If the CheckAnswer function for the question returns true...
            if (self.Correct+1) == self.DataSize:                                                                       #If the amount of questions correct (+1) = the amount of questions asked
                self.Display_Result()                                                                                   #Call the display_result function
                gui.destroy()                                                                                           #destroy the gui
            continuation = mb.askquestion("Result", "Would you like to walk away with ${}?".format(self.Counter))       #Offer the users to walk away from the game, winning the amount at stake
            self.Counter *= 2                                                                                           #Multiply the winnings by 2

            if continuation == 'yes':                                                                                   #If the user chooses yes....
                WinningAlert = "Congratulations, you have won ${}".format(int(round(self.Counter/2)))                   #Declare an alert that tells the user how much money they have won. The format is int(round(self.Counter/2)) as the counter multiplies by 2 before this command is executed.
                mb.showinfo("Result", f"{WinningAlert}")                                                                #Print a pop-up that displays the alert
                mb.showinfo("Action", "You will now be returned to the Home Screen")                                    #Display another pop up that informs the user that they will be returned to the home screen
                gui.destroy()                                                                                           #Destroys the GUI (as the game has finished)
            else:
                mb.showinfo("Continue", "Moving on to the Next Question")                                               #Display a pop-up that informs the user that they are moving to the next question
                time.sleep(2)                                                                                           #suspends the code execution for 2 seconds to lengthen the flow of the game
                mb.showinfo("Continue", "You are now playing for ${}".format(self.Counter))                             #Display a pop-up that tells the user how much the next question is worth.

        self.Correct += 1                                                                                               #Increment the correct questions by 1
        self.QuestionNumber = random.randint(0, self.DataSize)                                                          #Randomize another question from the json file.
        print(self.QuestionNumber)
        if self.QuestionNumber not in self.AskedList:                                                                   #if the randomised question number is not in the already asked list
            self.AskedList.append(self.QuestionNumber)                                                                  #add the question number to the list
            #print(self.AskedList)
        else:
            self.QuestionNumber = random.randint(0, self.DataSize)                                                      #randomize another question from the json file
            if self.QuestionNumber not in self.AskedList:                                                               # if the randomised question number is not in the already asked list
                self.AskedList.append(self.QuestionNumber)                                                              # add the question number to the list
                #print(self.AskedList)
            else:
                self.QuestionNumber = random.randint(0, self.DataSize)                                                  # randomize another question from the json file
                if self.QuestionNumber not in self.AskedList:                                                           # if the randomised question number is not in the already asked list
                    self.AskedList.append(self.QuestionNumber)                                                          # add the question number to the list
                    #print(self.AskedList)
                else:
                    self.QuestionNumber = random.randint(0,self.DataSize)                                               # randomize another question from the json file
                    if self.QuestionNumber not in self.AskedList:                                                       # if the randomised question number is not in the already asked list
                        self.AskedList.append(self.QuestionNumber)                                                      # add the question number to the list
                        #print(self.AskedList)
                    else:
                        self.QuestionNumber = random.randint(0,self.DataSize)                                           # randomize another question from the json file
                        if self.QuestionNumber not in self.AskedList:                                                   # if the randomised question number is not in the already asked list
                            self.AskedList.append(self.QuestionNumber)                                                  # add the question number to the list
                            #print(self.AskedList)

        if (self.Correct) == self.DataSize:                                                                             #If the user has answered the same amount of questions as the Data size (24)
            self.Display_Result()                                                                                       #Execute the Display_result function
        else:
            self.Display_Question()                                                                                     #call and execute the display_question function
            self.Display_Options()                                                                                      #call and execute the display_options function
            self.MoneyAtStake()                                                                                         #call and execute the MoneyAtStake function
            self.MoneyBoard()                                                                                           #call and execute the MoneyBoard function

    def Buttons(self):
        NextButton = Button(gui, text="Next", command=self.NextButton, width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))     #Declares what happens if the next button is pressed. If the button is pressed, the NextButton function is called
        NextButton.place(x=350, y=450) #places the button on the GUI at the x, y position

        Help_Button = Button(gui, text="Help", command=self.OpenWeb, width=5, bg="black", fg="white", font=("ariel", 16, " bold"))  #This button declares what happens if the Help button is pressed. If the button is pressed, the Help Website function is opened.
        Help_Button.place(x=700, y=60) #places the button on the GUI at the x, y position

        Quit_Button = Button(gui, text="Quit", command=self.QuitApp, width=5, bg="black", fg="white", font=("ariel", 16, " bold"))  #This button declares what happens if the Quit button is pressed. If the button is pressed, the Quit App function is called
        Quit_Button.place(x=700, y=90) #places the button on the GUI at the x, y position

    def Display_Options(self):                              #This function defines the displaying of each question.
        QuestionValue = 0                                   #Set the question value as 0
        self.Opt_Selected.set(0)
        for Option in Options[self.QuestionNumber]:         #For each option in the options for each question
            self.Opts[QuestionValue]['text'] = Option       #Set each individual text option as a possible option
            QuestionValue += 1                              #Add 1 to the question value.

    def Display_Question(self): #This function defines the question that is displayef on the screen
        QuestionNumber = Label(gui, text=Question[self.QuestionNumber], width=120, font=('ariel', 16, 'bold'), anchor='w') #Defines a label that shows the Question on the screen, with a certain font size and width
        QuestionNumber.place(x=70, y=225)   #Places the Question on the GUI Screen

    def Display_Title(self): #This function defines the title of the GUI
        Title = Label(gui, text="AI.EVC", width=50, bg="green", fg="white", font=("ariel", 20, "bold"))     #Create a label for title of the GUI
        Title.place(x=0, y=2)                                                                               #Place the title at the very top of the page.

    def Radio_Buttons(self): #This function prints the 4 options for each question that the user can choose from
        QuestionList = []                               #Creates an empty list that stores each question option.
        Y_Position = 275                                #Sets the Y position at 275
        while len(QuestionList) < 4:                    #While the length of the QuestionList is less than 4
            Radio_Button = Radiobutton(gui, text=" ", variable=self.Opt_Selected, value=len(QuestionList) + 1, font=("ariel", 14)) #Declares the variables of the Radio Button (
            QuestionList.append(Radio_Button)           #Add the Button to the Question List
            Radio_Button.place(x=100, y=Y_Position)     #place the button at a certain position on the GUI screen
            Y_Position += 40                            #Add 40 to the Y_Position, so the next button can be stored directly below the previous button
        return QuestionList                             #Return the Question List

    def MoneyAtStake(self): #This function defines the Money at Stake for each question.
        MoneyBand = Label(gui, text="Amount of money at stake: \n ${}".format(self.Counter), width=50, bg="green", fg="white", font=("ariel", 20, "bold")) #declares a label that tells the user the amount of money at stake for the specific question.
        MoneyBand.place(x=90, y=140) #places the label on the GUI

    def MoneyBoard(self): #a function that prints out the board showing all the money options at stake
        BoardCount = 0                  #Sets a counter for the positon of the money board
        BoardLabel = Label(gui, text="Money Board: ", width = 40, bg="green", fg="white", font=("ariel", 20, "bold")) #This defines the variables of the label (text, width, background, foreground etc.) This label defines what the below labels represent
        BoardLabel.place(x=860, y=10)   #This identifies the x and y positions of the BoardLabel i.e. where it is placed
        BoardList = []                  #An empty list that stores all of the labels below
        MaxMoney = 8388608              #This refers to the maximum amount of money that can be won, from answering all 24 questions correctly.
        Y_Position = 50                 #This is the position on the y axis for the money labels below
        Total_Boards = 23               #This refers to the maximum amount of questions that can be asked during the game (24). Remember, python counts 0 as the first character, therefore this variable is set as 23)

        while BoardCount < 24:
            AmountButton = Label(gui, text="${}".format(int(round(MaxMoney))), width=20, bg="red", fg="white", font=("ariel", 20, "bold")) #This defines the variables of a label, one that shows the Maximum amount of money that can be won for that specific question.
            BoardList.append(AmountButton)              #Adds the above button to the boardlist.
            AmountButton.place(x=1000, y=Y_Position)    #places the button on the GUI
            Y_Position += 30                            #adds 30 to the Y_Position variable, so the next label can be placed under the previous label
            MaxMoney /= 2                               #Divides the MaxMoney variable by 2 (as the money labels from top to bottom go from the highest value to the lowest value i.e. $8388608 to $1)
            BoardCount += 1                             #Add 1 to the BoardCount: go to the next variable

        if len(BoardList) > 0:                          #If the length of the boardlist is grater than 0...
            BoardList[len(BoardList)-1] = Label(gui, text="${}".format(self.Counter), width=20, bg="green", fg="white", font=("ariel", 20, "bold")) #This label represents the current amount of money that the user is playing for. It is highlighted in green to represent the current amount of money that the user is playing for.
            Counter = 30*(self.Correct+1)                                       #Multiply 30 by the correct question + 1., to move the y variable up by Counter
            BoardList[len(BoardList)-1].place(x=1000, y=Y_Position-Counter)     #Place the highlighted board on the position, reducing the y variable up by counter.
            Total_Boards -= 1                                                   #Reduce the total boards by 1 (i.e. move on the board above)
        return BoardList

gui = Tk()                              #Initialises the GUI as a Tkinter Window
gui.geometry("1500x1000")               #sets the size of the GUI window
gui.title("AI.EVC Quiz")                #sets the title of the GUI (shown at the top of the window)

with open('data.json') as f:            #opens the 'Data' file, containing all the Questions and its Answers
    Data = json.load(f)                 #loads the Data from the json file

Question = (Data['question'])           #sets the Question as parts of the json file that are under the 'Question' variable
Options = (Data['options'])             #sets the Options as parts of the json file that are under the 'Options' variable
Answer = (Data['answer'])               #sets the Answer as parts of the json file that are under the 'Answer' variable

quiz = Quiz()                           #calls the Quiz class so it can be executed

gui.mainloop()                          #a command that tells python to run the Tkinter event loop
                                        #this listens for events, such as processes or button clicks and blocks any code that comes after it from running until the window it is called on is closed.


