lista = [[1949, 112], [1949, 118], [1949, 132], [1949, 129], [1949, 121], [1949, 135], [1949, 148], [1949, 148], [1949, 136], [1949, 119], [1949, 104], [1949, 118], [1950, 115], [1950, 126], [1950, 141], [1950, 135], [1950, 125], [1950, 149], [1950, 170], [1950, 170], [1950, 158], [1950, 133], [1950, 114], [1950, 140], [1951, 145], [1951, 150], [1951, 178], [1951, 163], [1951, 172], [1951, 178], [1951, 199], [1951, 199], [1951, 184], [1951, 162], [1951, 146], [1951, 166]]


def generatore(first_year, last_year):
    x=0
    y=0
    
    for i in range(first_year, (last_year+1)):

        if(lista[x][0]==i):
            
            d = []
            for p in range(0,12):  
                d.append(lista[y][1])
                y+=1            
        else:
            continue
        
        x+=12
        yield d


    for i in generatore(1949,1951):
    
        return i

print(generatore(1949,1951))



"""
x=0
for i in generatore(1949,1951):
    
    if(i==lista[x][0]):
        i.append(lista[x][0])

    if(len(i)==12):
        i+=1

    print(i)
    x+=1
"""


lista_linee = []
for line in self.name:
    lista_linee.append(line)

contatore = 0
misuratore = 0
for line in self.name:
    
    for i in lista_linee:

        if (i == line):
            misuratore+=1

    if(misuratore > 1):
        raise ExamException(...)

    contatore += 1



