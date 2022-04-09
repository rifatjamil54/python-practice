# ''' Q: 2 - find the second largest number of the given list.
# Sample: [0, 1, 4, 'apple', 9, 16, 25, 'apple', 36, 81, 49, 'banana', 36, 49, 64]
# Expected output: 64 '''

list = [0, 1, 4, 'apple', 9, 16, 25, 'apple', 36, 81, 49, 'banana', 36, 49, 64]
int_item = []
for item in list:
    if type(item) == int:
        int_item.append(item)


int_item.sort()

print(int_item[-2])
