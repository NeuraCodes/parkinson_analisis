import sys
import os
import csv
import pandas as pd


def _convertDf(data):
    df = pd.read_csv(data)
    return df

def descData(data):
    dfCopy = _convertDf(data)
    dfCopy.head()

def convertData(archivo,delimiter=','):
    output_file = os.path.join('dataset/','parkinsons.csv')
    with open(archivo, 'r') as datafile, open(output_file,'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in datafile:
            row = line.strip().split(delimiter)
            csv_writer.writerow(row)
    
    print(f"Archvo creado en: {output_file}")


if '__main__' == __name__:

    if len(sys.argv) < 2:
        print('Pase el argumento para obtener los datos')
        sys.exit(1)

    #Convertir datos a csv
    #convertData(sys.argv[1])

    print(descData(sys.argv[1]))