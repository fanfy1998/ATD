import os.path
from os import path

def loadLabel():
    pasta = 'HAPT Data Set/RawData/labels.txt'
    f = open(pasta, 'r')
    labels = []
    for x in f:
        mini =[]
        aux = x.split(' ')
        for el in aux:
            mini.append(float(el))
        labels.append(mini)
    return labels
