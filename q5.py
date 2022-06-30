# Take key and value input from user, and add this key and value to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# after that if the value is even then make it odd or if the value is odd then print the value as like as 
# Expected Output:{0: 10, 1: 20, 3: 31}


loops = int(input("Enter item numbers in dictionary: "))

di = {}

for i in range(loops):
    ke = int(input("Enter key: "))
    val = int(input("Enter value: "))
    val += 1
    di.update({ke:val})


print(di)


