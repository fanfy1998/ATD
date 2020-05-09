import loadData
import loadLabels
import matplotlib.pyplot as plt
import numpy as np
import math

JANELA_DESLIZANTE = 0
AMOSTRASSEGUNDO = 50
STEP_FREQ = 50


def auxDft(todo,janela):
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
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    else:
                        break
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                andando.append(med)
        elif activities[int(element[0][0])-1] == activities[1]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    else:
                        break
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                subindoEscadas.append(med)
        elif activities[int(element[0][0])-1] == activities[2]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    else:
                        break
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                descendoEscadas.append(med)
        elif activities[int(element[0][0])-1] == activities[3]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    else:
                        break
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                sentado.append(med)
        elif activities[int(element[0][0])-1] == activities[4]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    else:
                        break
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                pe.append(med)
        elif activities[int(element[0][0])-1] == activities[5]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    else:
                        break
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                deitado.append(med)
        elif activities[int(element[0][0])-1] == activities[6]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                pesenta.append(med)
        elif activities[int(element[0][0])-1] == activities[7]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                sentape.append(med)
        elif activities[int(element[0][0])-1] == activities[8]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                sentadeita.append(med)
        elif activities[int(element[0][0])-1] == activities[9]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                deitasenta.append(med)
        elif activities[int(element[0][0])-1] == activities[10]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                pedeita.append(med)
        elif activities[int(element[0][0])-1] == activities[11]:
            for i in range(len(element[2])):
                aux = []
                window=0
                while window<=janela:
                    if i+window < len(element[2]):
                        aux.append(element[2][i+window])
                    window+=1
                if window>0:
                    med = float(sum(aux)/window)
                else:
                    med = sum(aux)
                deitape.append(med)
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
        plt.plot(np.linspace(begin,begin+len(element[2])/(60*AMOSTRASSEGUNDO),len(element[2])),element[2],linewidth=0.3)
        plt.ylim(top=max(element[2])+0.3)
        plt.ylim(bottom=min(element[2])-1)
        plt.text(begin, min(element[2])-0.7, activities[int(element[0][0])-1], fontsize = 10, fontname='DejaVu Sans')
        begin+=len(element[2])/(60*AMOSTRASSEGUNDO)
        #################312#####################
        plt.subplot(312)
        plt.ylabel("ACC_Y")
        plt.plot(np.linspace(begin2,begin2+len(element[3])/(60*AMOSTRASSEGUNDO),len(element[3])),element[3],linewidth=0.3)
        plt.ylim(top=max(element[3])+0.3)
        plt.ylim(bottom=min(element[3])-1)
        plt.text(begin2, min(element[3])-0.7, activities[int(element[0][0])-1], fontsize = 10, fontname='DejaVu Sans')
        begin2+=len(element[3])/(60*AMOSTRASSEGUNDO)
        #################313#####################
        plt.subplot(313)
        plt.ylabel("ACC_Z")
        plt.xlabel("Time (min)")
        plt.plot(np.linspace(begin3,begin3+len(element[4])/(60*AMOSTRASSEGUNDO),len(element[4])),element[4],linewidth=0.3)
        plt.ylim(top=max(element[4])+0.3)
        plt.ylim(bottom=min(element[4])-1)
        plt.text(begin3, min(element[4])-0.7, activities[int(element[0][0])-1], fontsize = 10, fontname='DejaVu Sans')

        begin3+=len(element[4])/(60*AMOSTRASSEGUNDO)
    plt.show()

def plotaDFT(arrayDFT):
    N = len(arrayDFT[0])
    plt.figure()
    plt.plot(np.linspace(0.0, N/AMOSTRASSEGUNDO, len(arrayDFT[0])), np.abs(arrayDFT[0]))
    plt.show()


def staticSteps(arrayDFT):
    plt.figure()

    quadro="31"
    aux=1

    i=3
    while i<6:
        if len(arrayDFT[i])>0:
            plt.subplot(int(quadro+str(aux)))
            plt.plot(np.linspace(0.0, len(arrayDFT[i])/AMOSTRASSEGUNDO, len(arrayDFT[i])), np.abs(arrayDFT[i]))
            arr = []
            while len(arr)<len(arrayDFT[i]):
                arr.append(STEP_FREQ)
            plt.plot(np.linspace(0.0, len(arrayDFT[i])/AMOSTRASSEGUNDO,len(arrayDFT[i])),arr)
            aux+=1
        i+=1
    sentado = []
    depe = []
    deitado = []

    j = 3

    while j<6:
        conta = 0
        instante = 0
        for i in range(len(arrayDFT[j])):
            if np.abs(arrayDFT[j][i])>STEP_FREQ:
                conta += 1
            if instante==50:
                if j==3:
                    sentado.append(conta)
                elif j==4:
                    depe.append(conta)
                else:
                    deitado.append(conta)
                conta=0
                instante=0
            instante+=1
        if j==0 and conta!=0:
            sentado.append(conta)
        elif j==1 and conta!=0:
            depe.append(conta)
        elif j==2 and conta!=0:
            deitado.append(conta)
        j+=1
    plt.show()

    return [sentado,depe,deitado]

def dinamicalSteps(arrayDFT):
    plt.figure()

    quadro="31"
    aux=1

    for i in range(3):
        if len(arrayDFT[i])>0:
            plt.subplot(int(quadro+str(aux)))
            plt.plot(np.linspace(0.0, len(arrayDFT[i])/AMOSTRASSEGUNDO, len(arrayDFT[i])), np.abs(arrayDFT[i]))
            arr = []
            while len(arr)<len(arrayDFT[i]):
                arr.append(STEP_FREQ)
            plt.plot(np.linspace(0.0, len(arrayDFT[i])/AMOSTRASSEGUNDO,len(arrayDFT[i])),arr)
            aux+=1
    pacosAndando = []
    pacosDescendo = []
    pacosSubindo = []

    for j in range(3):
        conta = 0
        instante = 0
        for i in range(len(arrayDFT[j])):
            if np.abs(arrayDFT[j][i])>STEP_FREQ:
                conta += 1
            if instante==50:
                if j==0:
                    pacosAndando.append(conta)
                elif j==1:
                    pacosDescendo.append(conta)
                else:
                    pacosSubindo.append(conta)
                conta=0
                instante=0
            instante+=1
        if j==0 and conta!=0:
            pacosAndando.append(conta)
        elif j==1 and conta!=0:
            pacosDescendo.append(conta)
        elif j==2 and conta!=0:
            pacosSubindo.append(conta)
    plt.show()

    return [pacosAndando,pacosSubindo,pacosDescendo]


def main():
    activities=['WALK','WALK_UP','WALK_DOWN','SIT','STAND','LAY','STAND_SIT','SIT_STAND','SIT_LIE','LIE_SIT','STAND_LIE',"LIE_STAND"]
    data = loadData.loadData()
    labels = loadLabels.loadLabel()
    exp = 22
    user = 11
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


    paiX = auxDft(todo,JANELA_DESLIZANTE)
    arrayDFT = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(paiX)):
        for k in range(len(paiX[i])):
            arrayDFT[i].append(dft(paiX[i], k))

    #plota(todo)
    #plotaDFT(arrayDFT)
    '''pacosEstaticos= staticSteps(arrayDFT)
    pacosDinamicos=dinamicalSteps(arrayDFT)
    walkMean = np.mean(pacosDinamicos[0])
    upMean = np.mean(pacosDinamicos[1])
    downMean = np.mean(pacosDinamicos[2])
    walkdp = np.std(pacosDinamicos[0])
    updp = np.std(pacosDinamicos[1])
    downdp = np.std(pacosDinamicos[2])
    print("MEDIA ANDANDO= "+str(walkMean))
    print("MEDIA SUBINDO= "+str(upMean))
    print("MEDIA DESCENDO= "+str(downMean))
    print("DESVIO-PADRÃO ANDANDO= "+str(walkdp))
    print("DESVIO-PADRÃO SUBINDO= "+str(updp))
    print("DESVIO-PADRÃO DESCENDO= "+str(downdp))'''



main()
