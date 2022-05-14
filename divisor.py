def divisors (item):
    divisorList = [ i for i in range(1,item+1) if item % i == 0]
    return divisorList

dv = divisors(int(input("Please choose a number to divide: ")))    
print(dv)
