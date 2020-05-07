import os.path
from os import path
def loadData():
    pasta = 'HAPT Data Set/RawData/'
    arrUser = ['10','11','12','13','14','15']
    arrExp = ['21','22','23','24','25','26','27','28','29','30']
    auxIndex = 0

    dici = {}
    for user in arrUser:
        while auxIndex<len(arrExp) and path.exists(pasta+'acc_exp'+arrExp[auxIndex]+'_user'+user+'.txt'):
            f = open(pasta+'acc_exp'+arrExp[auxIndex]+'_user'+user+'.txt', "r")
            loadedData = []
            linha=0
            for x in f:
                miniArr = []
                aux = x.split(' ')
                for el in aux:
                    miniArr.append(float(el))
                loadedData.append(miniArr)
                linha+=1
            f.close()
            dici['acc_exp'+arrExp[auxIndex]+'_user'+user+'.txt']=loadedData
            auxIndex += 1
    return dici
