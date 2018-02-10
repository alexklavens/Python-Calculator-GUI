# button.py
# for lab 9 on writing classes

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        "Sets this button to 'inactive'."
        ##color the text "darkgray"
        ##set the outline to look finer/thinner
        ##set the boolean variable that tracks "active"-ness to False
        self.label.setFill('darkgray')
        self.rect.setWidth(0.5)
        self.active = False
    ##check 4.  complete the clicked() method
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        ##your code here
        
        if (self.xmin <= p.getX() <= self.xmax) \
           and (self.ymin <= p.getY() <= self.ymax) and self.active:
            return True
        else:
            return False

    def setLabelSize(self,fontSize):
        self.label.setSize(fontSize)

'''
def main():
    ##check 1. create a graphical window in which to test the Button class
    win=GraphWin("diceroller",600,600)
    
    ##check 2. test the Button constructor method...
    ##create two Button objects, one for "Roll Dice" and the other for "Quit"
    ##activate the Roll button
    rolldiceBtn=Button(win,Point(200,400),90,50,'Roll Dice')
    quitBtn=Button(win,Point(400,400),50,50,'Quit')
    ##check 3. now test the deactivate() method...
    ##deactivate the "Quit" button
    quitBtn.deactivate()
    ##check 4. test the .clicked() method with an if statement
    ##(remove this test code before moving onto the next check)
    pt = win.getMouse()
    
    ##check 5. now test the clicked() boolean method...
    ##keep taking mouse clicks (in a loop) until the "Quit" button is clicked
        ##if the roll button is clicked
            ##activate the quit button
    while not quitBtn.clicked(pt):
        
        if rolldiceBtn.clicked(pt):
            rolldiceBtn.activate()
            quitBtn.activate()
        pt=win.getMouse()
    #we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__":
    main()
'''
