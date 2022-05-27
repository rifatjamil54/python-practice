# ''' Q: 1 - You have to find 49 from this list. If 49 exists on the list, then count the number.
# Sample: [0, 1, 4, 'apple', 9, 16, 25, 'apple', 36, 81, 49, 'banana', 36, 49, 64]
# Expected output: 2 '''


list = [0, 1, 4, 'apple', 9, 16, 25, 'apple', 36, 81, 49, 'banana', 36, 49, 64]
num = []
for i in list:
    if i == 49:
        num.append(i)
        
print(len(num))