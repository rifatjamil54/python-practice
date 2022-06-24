class Mobile: #Creat class
    def __init__(self): #init  method/function
        self.model = "RealMe" # A instance variablle
    def show_model(self): # instantce method
        self.model # accessing instance variable

realme = Mobile() #creat Object

a = realme.model # call instance variable

print(a)