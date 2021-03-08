import random
import string

adjectives = ['big', 'small', 'nice', 'large',
              'huge', 'green', 'yellow', 'sweet']
nomen = ['sun', 'star', 'sky', 'computer', 'tee', 'coffee']

print('welcome to the password generator')

while True:
    adjectives = random.choice(adjectives)
    nomen = random.choice(nomen)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjectives + nomen + str(number) + special_char
    print('The new password is: %s' % password)

    anather_password = input('Do you want another password (yes or no)?')
    if anather_password == 'no':
        break
