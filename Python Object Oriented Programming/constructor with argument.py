class Mobile:
    def __init__(self, m, v=80 ):
        self.model = m
        self.volumn = v

    def show_model(self, p):
        price = p
        print("Model:", self.model)    
        print("Volunm:", self.volumn)

realme = Mobile("RealMe X")        
realme.show_model(1000)