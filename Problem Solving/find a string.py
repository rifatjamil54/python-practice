

def count_the_substring(string, sub_stiring):
    c = 0
    l = len(sub_stiring)
    for i in range(len(string)):
        s = string[i:i+l]
        if s == sub_stiring:
            c = c + 1
    return c


s = 'ABCDCDC'

ss = 'CDC'

re = count_the_substring(s,ss)

print(re)
