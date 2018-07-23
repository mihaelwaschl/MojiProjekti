import random

def read_file(file):
    readed_file = open(file, 'r', encoding='UTF-8')
    text = readed_file.read()
    readed_file.close()
    return text

def greb_word():
    list_of_items = read_file('besede.txt').split('\n')
    print(list_of_items)
    return list_of_items[int(random.uniform(0, len(list_of_items)))]

