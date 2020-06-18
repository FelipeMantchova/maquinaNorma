import re

A = 0 
B = 0 
C = 0 
D = 0 
i = 0

lista = []

def Norma(arquivo):
    global A ,B, C, D, i, lista
    with open(arquivo, "r") as arq:
        lista = arq.readlines()
    setValReg(lista[0])
    return lerInstrucao(lista[1], True)
        

def lerInstrucao(linha, continua):
    global A ,B, C, D, i, lista

    if continua is False:
        return 1 

    pattern = re.compile(r'([0-9]+):([A-Z]{3}) ([A-Z]) ([0-9]+)\s?([0-9]+)?')
    matches = pattern.findall(linha)

    rotulo = int(matches[0][0])
    instrucao = matches[0][1]
    registrador = matches[0][2]
    jump = int(matches[0][3])
    if matches[0][4]:
        condJump = int(matches[0][4])

    if instrucao == "ADD":
        printInstrucao(rotulo)
        ADD(registrador)
        return lerInstrucao(lista[jump], True)
    elif instrucao == "SUB":
        printInstrucao(rotulo)
        SUB(registrador)
        return lerInstrucao(lista[jump], True)
    elif instrucao == "ZER":
        printInstrucao(rotulo)
        if ZER(registrador):
            if jump == 404:
                return lerInstrucao(lista[0], False)
            return lerInstrucao(lista[jump], True)
        else:
            return lerInstrucao(lista[condJump], True)
    
    
    

def ZER(registrador): 
    global A ,B, C, D 
    if registrador == "A" and A == 0:
        return True
    elif registrador == "B" and B == 0:
        return True
    elif registrador == "C" and C == 0:
        return True
    elif registrador == "D" and D == 0:
        return True
    return False
  
def ADD(registrador):
    global A ,B, C, D 
    if registrador == "A":
            A += 1  
    elif registrador == "B":
            B += 1
    elif registrador == "C":
            C += 1
    else:
            D += 1
    
           
def SUB(registrador):
    global A ,B, C, D 
    if registrador == "A":
            A -= 1  
    elif registrador == "B":
            B -= 1
    elif registrador == "C":
            C -= 1
    else:
            D -= 1
    

def setValReg(linha):
    global A ,B, C, D
    pattern = re.compile(r'\d')
    matches = pattern.findall(linha)
    A = int(matches[0])
    B = int(matches[1])
    C = int(matches[2])
    D = int(matches[3])
    printInstrucao("M")
    

def printInstrucao(linha):
    print("(" + str(A) + ", " + str(B) + ", " + str(C) + ", " + str(D) + ") "+ str(linha) + ")")
   