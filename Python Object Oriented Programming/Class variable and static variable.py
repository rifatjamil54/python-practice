class Mobile:
    fp = "Yes" # class variable

    def __init__(self) -> None:
        self.model = "RealMe X"  # instance variable

    def show_model(self):   # inctence method
        print("Model : ",self.model) # accessing instance variable

    @classmethod     # class method
    def is_fp(cls):
        print("Finger Print", cls.fp)  # accessing instance variable

realmme = Mobile() # creat objeect
realmme.show_model # call instance method
Mobile.is_fp() # call class method