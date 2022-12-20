children = ["Bill","David","Susan","Jane","Kent","Brad"]

turnover = 7
index_shift = 0

for i in range(len(children),1,-1):

    index = (turnover%i+index_shift)%i
    print(children.pop(index), 'moves')
    index_shift = index

print(children[0], 'is the winner')
