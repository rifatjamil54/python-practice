#  Q: 3 - Remove apple from the list
# Sample: [0, 1, 4, 'apple', 9, 16, 25, 'apple', 36, 81, 49, 'banana', 36, 49, 64]
# Expected output: [0, 1, 4, 9, 16, 25, 36, 81, 49, 'banana', 36, 49, 64]

list = [0, 1, 4, 'apple', 9, 16, 25, 'apple', 36, 81, 49, 'banana', 36, 49, 64]
output_list = []
for i in list:
    if i != 'apple':
        output_list.append(i)

print(output_list)
