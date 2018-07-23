def read_file(file):
    readed_file = open(file, 'r', encoding='UTF-8')
    text = readed_file.read()
    readed_file.close()
    return text

def greb_word(text_file):
    