n = int(input('input;').strip())

even = n % 2

if even == 0 and n > 2 and n < 5:
    print('Not Weird')
elif even == 0 and n > 20:
    print('Not Weird')
else:
    print('Weird')    
