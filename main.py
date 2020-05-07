import loadData
import loadLabels
import matplotlib.pyplot as plt
import numpy as np
import math


def auxDft(todo):
    activities=['WALK','WALK_UP','WALK_DOWN','SIT','STAND','LAY','STAND_SIT','SIT_STAND','SIT_LIE','LIE_SIT','STAND_LIE',"LIE_STAND"]
    andando=[]
    subindoEscadas=[]
    descendoEscadas=[]
    sentado=[]
    pe=[]
    deitado=[]
    pesenta=[]
    sentape=[]
    sentadeita=[]
    deitasenta=[]
    pedeita=[]
    deitape=[]
    for element in todo:
        if activities[int(element[0][0])-1] == activities[0]:
            for elem in element[2]:
                andando.append(elem)
        elif activities[int(element[0][0])-1] == activities[1]:
            for elem in element[2]:
                subindoEscadas.append(elem)
        elif activities[int(element[0][0])-1] == activities[2]:
            for elem in element[2]:
                descendoEscadas.append(elem)
        elif activities[int(element[0][0])-1] == activities[3]:
            for elem in element[2]:
                sentado.append(elem)
        elif activities[int(element[0][0])-1] == activities[4]:
            for elem in element[2]:
                pe.append(elem)
        elif activities[int(element[0][0])-1] == activities[5]:
            for elem in element[2]:
                deitado.append(elem)
        elif activities[int(element[0][0])-1] == activities[6]:
            for elem in element[2]:
                pesenta.append(elem)
        elif activities[int(element[0][0])-1] == activities[7]:
            for elem in element[2]:
                sentape.append(elem)
        elif activities[int(element[0][0])-1] == activities[8]:
            for elem in element[2]:
                sentadeita.append(elem)
        elif activities[int(element[0][0])-1] == activities[9]:
            for elem in element[2]:
                deitasenta.append(elem)
        elif activities[int(element[0][0])-1] == activities[10]:
            for elem in element[2]:
                pedeita.append(elem)
        elif activities[int(element[0][0])-1] == activities[11]:
            for elem in element[2]:
                deitape.append(elem)
    return [andando, subindoEscadas, descendoEscadas, sentado, pe, deitado, pesenta, sentape, sentadeita, deitasenta, pedeita, deitape]

def dft(x,k):
    transformada = 0
    for i in range(len(x)):
        transformada += (math.e**(-2*math.pi*1j*k*i/len(x)))*x[i]
    return transformada

def plota(todo):
    activities=['WALK','WALK_UP','WALK_DOWN','SIT','STAND','LAY','STAND_SIT','SIT_STAND','SIT_LIE','LIE_SIT','STAND_LIE',"LIE_STAND"]
    plt.figure()
    begin = 0
    begin2 = 0
    begin3 = 0
    for element in todo:
        #################311#####################
        plt.subplot(311)
        plt.ylabel("ACC_X")
        plt.plot(np.linspace(begin,begin+len(element[2])/1000,len(element[2])),element[2],linewidth=0.3)
        plt.ylim(top=max(element[2])+0.3)
        plt.ylim(bottom=min(element[2])-1)
        plt.text(begin, min(element[2])-0.7, activities[int(element[0][0])-1], fontsize = 10, fontname='DejaVu Sans')
        begin+=len(element[2])/1000
        #################312#####################
        plt.subplot(312)
        plt.ylabel("ACC_Y")
        plt.plot(np.linspace(begin2,begin2+len(element[3])/1000,len(element[3])),element[3],linewidth=0.3)
        plt.ylim(top=max(element[3])+0.3)
        plt.ylim(bottom=min(element[3])-1)
        plt.text(begin2, min(element[3])-0.7, activities[int(element[0][0])-1], fontsize = 10, fontname='DejaVu Sans')
        begin2+=len(element[3])/1000
        #################313#####################
        plt.subplot(313)
        plt.ylabel("ACC_Z")
        plt.plot(np.linspace(begin3,begin3+len(element[4])/1000,len(element[4])),element[4],linewidth=0.3)
        plt.ylim(top=max(element[4])+0.3)
        plt.ylim(bottom=min(element[4])-1)
        plt.text(begin3, min(element[4])-0.7, activities[int(element[0][0])-1], fontsize = 10, fontname='DejaVu Sans')
        begin3+=len(element[4])/1000
    plt.show()

def main():
    activities=['WALK','WALK_UP','WALK_DOWN','SIT','STAND','LAY','STAND_SIT','SIT_STAND','SIT_LIE','LIE_SIT','STAND_LIE',"LIE_STAND"]
    data = loadData.loadData()
    labels = loadLabels.loadLabel()
    exp = 21
    user = 10
    aux1 = 0
    aux2=0
    todo = []
    for element in labels:
        if element[0]==exp and element[1]==user:
            aux = []
            aux.append([element[2]])
            aux.append([element[3], element[4]])
            todo.append(aux)
    for i in range(len(todo)):
        inicio = int(todo[i][1][0])-1
        fim = int(todo[i][1][1])
        auxi=[]
        auxi2=[]
        auxi3=[]
        while inicio<fim:
            auxi.append(data['acc_exp'+str(exp)+'_user'+str(user)+'.txt'][inicio][0])
            auxi2.append(data['acc_exp'+str(exp)+'_user'+str(user)+'.txt'][inicio][1])
            auxi3.append(data['acc_exp'+str(exp)+'_user'+str(user)+'.txt'][inicio][2])
            inicio+=1
        todo[i].append(auxi)
        todo[i].append(auxi2)
        todo[i].append(auxi3)

    #plota(todo)
    paiX = auxDft(todo)
    arrayDFT = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(paiX)):
        for k in range(len(paiX[i])):
            arrayDFT[i].append(dft(paiX[i], k))
    print(arrayDFT)

main()
