class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return (self.a + self.b)

    def sub(self):
        return (self.a - self.b)

    def mul(self):
        return(self.a * self.b)

    def div(self):
        return(self.a / self.b)



x = int(input("Enter first number: "))

op = input("Oparetion: ")

y = int(input("Enter second number: "))


cal = Calculator(x,y) 


even_list = []

odd_list = [] 


dict = {"even": even_list, "odd": odd_list}

if op == "+":
    value = cal.add()
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)


elif op == "-":
    value = cal.sub()
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)


elif op == "*":
    value = cal.mul()
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)


elif op == "/":
    value = cal.div()
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)


else:
    print("Invalid Oparetion")


print(dict)

