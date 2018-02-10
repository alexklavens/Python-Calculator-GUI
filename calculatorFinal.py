#calculatorFinal.py
#Sam Barnes, Alex Klavens
#12/2/15
#This program runs a GUI based calculator

""" The calculator class will allow the user to perform calculations!"""
from graphics import*
from buttonclass import*
from time import*

class Calc: #creates calculator class
    
    """constructor method creates the visual display of a calculator
       and provides a GUI for simple mathmatical opperations"""

    def __init__(self): #Initualize class
        
        win = GraphWin("Calculator",250,400) #create calculator widow
        win.setCoords(0,0,90,120) #set coordinates
        win.setBackground("darkorange") #set color
        self.win = win #initualize win to self.win
        self.calcGUI() #call module to make buttons
        self._makeDisplay() #call module to make calculator display 
        self.myNumsList = [self.zeroButton,self.oneButton,self.twoButton,
                           self.threeButton,self.fourButton,self.fiveButton,
                           self.sixButton,self.sevenButton,self.eightButton,
                           self.nineButton,self.clearButton,self.addButton,
                           self.subButton,self.divButton,self.chooseButton,
                           self.negButton,self.multiButton,self.expoButton,
                           self.equalButton,self.decButton,self.closeButton,
                           self.baseButton] #all of the buttons kept in list

    """_expoNums() takes two numbers and returns the value of
       of the first number to the power of the second number"""
    def _expoNums(self,n,e): #function to find exponents recursively
        if e == 0: #if the exponent is zero:
            return 1 #n to the zero is 
        else: #if the explonent isnt 0
            factor = self._expoNums(n,e//2) #call function recursively with half
                                            #of the exponent each time
            if e%2 == 0: #if exponent is even
                return factor * factor #then multiply the two half exponents to
                                       #get the full
            else:
                return factor*factor*n #multiply two half exponents and one
                                       #extra n

    def Choose(self,n,k): #solve n choose k recursively
        if k == 1: #when you choose 1 from n you get n
            return n
        elif n<k: #if k is ever less than n 
            return 0 #you get 0
        else:
            return self.Choose(n-1,k-1) + self.Choose(n-1,k) #formula for choose

    """Working in conjunction with _changeBase, _getBase returns
       a list of numbers that would compose a represntation of n in base b

       takes (n,b,lst) from _changeBase method"""
    def _getBase(self,n,b,lst): #recursively find convert base
        if n<b: #if the number being looked at is less than the base
            lst.insert(0,n) #add it to the fist position of the list
                            #this will be the fist thing added always
            return n #return n to solve the rest
        else:
            lst.insert(0,n%b) #add remainder to the front of the list
            return self._getBase(n//b,b,lst) #call function on n//b, which is
                                             #the number of times n fits in
                                             #whatever place it is in

    """_changeBase returns a string of the represntation of n in base b """

    def _changeBase(self,n,b): #another module needed to keep track of list
        l=[] #empty list
        self._getBase(n,b,l) #call getBase initially
        stri = "" #empty string
        for i in range(len(l)): #for every i between 0 and the length of the list
            if i == len(l)-1: #if it is the last item in the list
                stri = stri + str(l[i]) #add to string without space
            else:
                stri = stri + str(l[i]) + " " #add to string with space
        return stri #strung the string to where _changeBase is called
    
    """Returns the string of a number button that has been clicked """
    def _ifClicked(self): #determine what is clicked
        while True: #indefinate loop
            pt = self.win.getMouse() #get mouse click and point
            for button in self.myNumsList: #check every button
                if button.clicked(pt) == True: #if the button is clicked
                    return button.getLabel() #return the label

    """creates a display in the calculator"""

    def _makeDisplay(self): #creates the number display
        myDisp = Rectangle(Point(2,90),Point(65,65)) #creates rectangle
        myDisp.draw(self.win) #draw rectangle
        myDisp.setFill("white") #make it white
        text=Text(Point(35,75),'') #create emptry text box
        text.draw(self.win) #draw text box
        text.setStyle('bold') #set text tryle
        text.setSize(17) #set text size
        text.setFill('blue') #set text color
        self.display=text #make the text box accessable elsewhere in the class

    """_useButton updates the display, output results if certain buttons are
       clicked and takes into account non-python opperations (choose,<-,^)"""
    def _useButton(self,key): # make buttons work
        text = self.display.getText() #set the text to what is in display
        if key == 'AC': #if all clear key is clicked
            self.display.setText("") #clear the text
        elif key == '<-': #if backspace key is clicked
            self.display.setText(text[:-1]) #remove last character
        elif key == '=': #if equals is clicked
            if "^" in text: #if the exponent symbol is in the string
                try: #if it doesnt error
                    text = text.split("^") #split at exponent to get number being
                                           #raised to a power (right) and the power (left)
                    text = self._expoNums(eval(text[0]),eval(text[1])) #call module
                    result = text #set result to whatever is outputted by expoNums
                except: #if it does error
                    result = "ERROR" #set result to error

            elif "Choose" in text: #Same as above
                try:
                    text = text.split("Choose")
                    text = self.Choose(eval(text[0]),eval(text[1]))
                    result = text
                except:
                    result = "ERROR"
            elif 'b' in text: #Same as above

                text = text.split("b")
                text = self._changeBase(eval(text[0]),eval(text[1]))
                result = text

            else: #for all other keys
                try: #if it doesnt error
                    result=eval(text) #evaluate the string and set to result
                except: #if it does error
                    result = 'ERROR' #set result to error
            self.display.setText(str(result)) #set the text of the calculator to be the result
        else: #if equals clear or backspace are not clicked simply add the key to
            self.display.setText(text+key) #the string being displayed

    """operate() method runs the program in a while loop that breaks
       if the exit button is clicked"""

    def operate(self): #closes calculator is needed
        key = ""
        while key != "X": #if the key is not set to X

            key = self._ifClicked() #set key to the new clicked button
            self._useButton(key) #use that button
        self.win.close() #close if exit while loop

    """ calcGUI() creates the buttons. this is called in the constructor"""

    def calcGUI(self): #run the GUI
        x = 80 #initially set x to 80
        y = 7 #initially set y to 7 (if change needed)

        #create all of the buttons individually
        self.clearButton = Button(self.win,Point(x,100),20,15,"AC")
        self.addButton = Button(self.win,Point(x,85),20,15,"+")
        self.subButton = Button(self.win,Point(x,70),20,15,"-")
        self.divButton = Button(self.win,Point(x,55),20,15,"/")
        self.multiButton = Button(self.win,Point(x,40),20,15,"*")
        self.expoButton = Button(self.win,Point(x,25),20,15,"^")
        self.equalButton = Button(self.win,Point(x,7),20,15,"=")

        self.sevenButton = Button(self.win,Point(12,y+45),20,15,"7")
        self.eightButton = Button(self.win,Point(32,y+45),20,15,"8")
        self.nineButton = Button(self.win,Point(52,y+45),20,15,"9")

        self.fourButton = Button(self.win,Point(12,y+30),20,15,"4")
        self.fiveButton = Button(self.win,Point(32,y+30),20,15,"5")
        self.sixButton = Button(self.win,Point(52,y+30),20,15,"6")

        self.oneButton = Button(self.win,Point(12,y+15),20,15,"1")
        self.twoButton = Button(self.win,Point(32,7+15),20,15,"2")
        self.threeButton = Button(self.win,Point(52,y+15),20,15,"3")

        self.zeroButton = Button(self.win,Point(12,y),20,15,"0")
        self.chooseButton = Button(self.win,Point(32,y),20,15,"Choose")
        self.decButton = Button(self.win,Point(47+10,7),10,15,".")
        self.baseButton = Button(self.win,Point(47+19,7),8,15,"b")

        self.negButton = Button(self.win,Point(47,y),10,15,"<-")
        self.closeButton = Button(self.win,Point(5,115),6,5,"X")
        self.closeButton.rect.setFill('darkgrey')



def main(): #main function
    
    myCalc = Calc() #create instance of the class
    myCalc.operate() #run operate to run calcultor



if __name__ == "__main__":
    main()
        
