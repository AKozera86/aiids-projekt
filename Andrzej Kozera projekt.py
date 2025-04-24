

def open_file(filename: str, header=True, delimiter=';'):
    import csv
    labels=[]
    data=[]
    
    with open(filename, 'r') as uchwyt:
        dane=csv.reader(uchwyt, delimiter=delimiter)
        for i, row in enumerate(dane):
            if header and i==0:
                labels=row
            else:
                data.append(row)
    return data, labels



def etykiety(labels):
    
    if not labels:
        print("W pliku nie ma etykiet")
    else:
        print('W pliku znajdują się kolumny z etykietami:', labels)

def pokaz_dane(data, start=0, end=0):
    
    if end == 0:
        end=len(data)
    if start<end:
        for i in range(start, end):
            print(data[i])
    else:
        print("Proszę podaj prawodłowy zakres danych")

def podzial_danych(data, zt=0.0, zte=0.0, zw=0.0):
    import random as rd
    
    if zt+zte+zw==1.0 and zt>=0.0 and zte>=0.0 and zw>=0.0:
        zte=int((zte+zt)*len(data))
        zt=int(zt*len(data))
        rd.shuffle(data)
                
        zbior_treningowy=data[:zt]
        zbior_testowy=data[zt:zte]
        zbior_walidacyjny=data[zte:]
        return zbior_treningowy, zbior_testowy, zbior_walidacyjny
    
        
    else:
        print("proszę podaj poprawny podział danych sumujacy sie do 1")

def klasy_decyzyjne(data, labels, index:int):
    if index<=len(labels)-1:
        lista=[]
        for i in range(len(data)):
            lista.append(data[i][index])
        klasy=set(lista)
        for j in klasy:
            print((j, lista.count(j)))
    else:
        print("w pliku nie ma tylu kolumn")
            
def pokaz_klase(data, klasa:str, index:int):
    if index<=len(data[1])-1:
        for i in range(len(data)):
            if data[i][index]==klasa:
                print(data[i])
    else:
        print("w pliku nie ma " , index , "kolumn")

def zapisz(zbior: list, nazwa:str):
    plik=open(nazwa, 'w')
    for i in zbior:
        plik.write(';'.join(i) + '\n')
    plik.close()
            

def main():
    data, labels = open_file('winequality-red.csv')
    etykiety(labels)
    pokaz_dane(data, start=3, end=5)
    zbior_treningowy, zbior_testowy, zbior_walidacyjny = podzial_danych(data, 0.6, 0.2, 0.2)
    klasy_decyzyjne(data, labels, 11)
    pokaz_klase(data, "8", 11)
    zapisz(zbior_treningowy, 'zbior_treningowy.csv')
     
if __name__ == "__main__":
    main()
