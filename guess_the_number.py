import random
c = 0
def counter():
    global c
    c = c + 1
    return c

correct = 'Winner'


too_low = 'too low!!'

too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10

def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            userInput = int(input('Guess the secret number? '))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            return userInput


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''

    if guess == secret:
        print ("It took you " + str(c) + " tries")
        return correct

    if guess < secret:
        counter()
        #print (c)
        return too_low

    if guess > secret:
        counter()
        #print(c)
        return too_high

def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)


        if result == correct:
            break

if __name__ == '__main__':
    main()
