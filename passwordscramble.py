word = input()
password = ''

# FIXME - I am sure there is a more efficient way to do this than a pile of IF statements. To be researched.
for i in word:
    if i == 'i':
        password = password + '!'
    elif i == 'a':
        password = password + '@'
    elif i == 'm':
        password = password + 'M'
    elif i == 'B':
        password = password + '8'
    elif i == 'o':
        password = password + '.'
    else:
        password = password + i
   


print("{}q*s".format(password))
