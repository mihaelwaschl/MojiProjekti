import random

def read_file(file):
    readed_file = open(file, 'r', encoding='UTF-8')
    text = readed_file.read()
    readed_file.close()
    return text

def greb_random_word(list_items):
    list_of_items = read_file(list_items).split('\n')
    return list_of_items[int(random.uniform(0, len(list_of_items)))]

def start_game(word):
    for i in range(len(word)):
        letter = input().strip()
