def printTable(data):
    col_width = [0] * len(data)
    for i in range(len(data)):
        col_width[i] = max(data[i], key=len)
    longest = len(max(col_width, key=len))

    for x in range(len(data[0])):
        print(str(data[0][x].rjust(longest)) + str(data[1][x].rjust(longest)) + str(data[2][x].rjust(longest)))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)