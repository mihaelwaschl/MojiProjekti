import random

def read_file(file):
    readed_file = open(file, 'r', encoding='UTF-8')
    text = readed_file.read()
    readed_file.close()
    return text

def get_word():
    list_of_items = read_file('besede.txt').split('\n')
    return list_of_items[int(random.uniform(0, len(list_of_items)-1))]

def check(word, guess, guesses):
    guessed_word = ''
    matches = 0
    for letter in word:
        if letter in guesses:
            guessed_word += letter
        else:
            guessed_word += '*'
        if letter == guess:
            matches += 1
    if matches == 0:
        print('Poiskusi ponovno, v besedni ni črke {}!'.format(guess))
    elif matches == 1:
        print('V besedi se nahaja ena črka {}'.format(guess))
    elif matches == 2:
        print('V besedi se nahajata dve črki {}'.format(guess))
    else:
        print('V besedi se nahajajo {} črke {}'.format(matches, guess))
    return guessed_word

def start_game():
    word = get_word()
    guesses = []
    print('Beseda ima {} znakov, da odkriješ skrito besedo imaš {} poiskusov.'.format(len(word), len(word)+5))
    print('Vstavljate lahko posamezne črke, ali celotno besedo.')
    for i in range(len(word)+5):
        guess = input('Vnesi črko. \n').strip().lower()
        if guess in guesses:
            print('Črko {} si že uporabil. Poiskusi ponovno!'.format(guess))
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word, guess, guesses)
            if result == word:
                print('Čestitamo našli ste skrito besedo!')
                break
            else:
                print(result)
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                print('Čestitamo našli ste skrito besedo!')
                break
            else:
                print('Beseda {} žal ni pravilna, poiskusi ponovno'.format(guess))
        else:
            print('Beseda {} ni ustrezne dolžine.'.format(guess))
    print('Konec igre, skrita beseda je {}'.format(word))


start_game()



