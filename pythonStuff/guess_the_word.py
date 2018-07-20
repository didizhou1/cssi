

word = 'programming'
guess = ''
letters = ''
for char in word:
    guess += '_'

while (guess != word):
    currentGuess = '';
    print(guess)
    print('Guesses: '+letters)
    currentGuess += input('Guess a letter: ')
    pos=0
    count=0
    for char in word:
        if currentGuess == char:
            new = list(guess)
            new[pos]=currentGuess
            guess = ''.join(new)
            count+=1
        pos+=1
    if count == 0:
        letters+=currentGuess

print('You win!')
