import random

def roll_dice():
    start_rolling = True
    while start_rolling:
        pick_number = int(random.uniform(1,7))
        print('Na kocki se je pokazala številka {}\n'.format(pick_number))
        ponovna_igra = input('Želiš še enkrat vreči kocko? Vpiši y za ja in n za ne.')
        if ponovna_igra == 'n':
            start_rolling = False

roll_dice()