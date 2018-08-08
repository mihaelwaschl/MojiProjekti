import csv,time, math

razdalja = []
count = 0
timestr = time.strftime("%d%m%Y-%H%M%S")

with open('Bossssok1.csv', newline='') as csvfile:
     file = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in file:
         data = ''.join(row)
         try:
             splited = data.replace(',', '.').split(';')
             x1 = float(splited[0]) - 545.0
             y1 = float(splited[1]) - 988
             x2 = float(splited[2]) * float(0.1)
             y2 = float(splited[3]) * float(0.1)
             razdalja.append(math.sqrt((x2 - x1)**2 + (y2 -y1)**2))
             count += 1
         except ValueError:
             razdalja.append('V vrstici {} jr prišlo je do, napake preveri vhodne podatke!'.format(count))
             count += 1

with open('rezultati{}.csv'.format(timestr), 'w', newline='') as csvfile:
    result = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in razdalja:
        replace = str(row).replace('.', ',')
        result.writerow([replace])
