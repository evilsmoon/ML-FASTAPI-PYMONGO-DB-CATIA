import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re
import numpy as np
import json
import math
# import ntlk
from config.db import  conn
from schemas.sorter import sorterEntity,sortersEntity
sw = stopwords.words('spanish')
def lowercase():
  
    db_sorter =  sortersEntity(conn.catia.sorter.find({}))
    data_A = []
    data_B = []
    data_C = []
    for i in range(len(db_sorter)):
        if db_sorter[i]['name'] == 'MODELO BIO MEDICO':
            data_A.append(db_sorter[i]['data'])
            for n in db_sorter[i]['data']:
                data_A = n.lower()
        elif db_sorter[i]['name'] == 'ENFOQUE PSICOSOCIAL - COMUNITARIO':
            for n in db_sorter[i]['data']:
                data_B = n.lower()
        elif db_sorter[i]['name'] =='ENFOQUE COTIDIANO':
            for n in db_sorter[i]['data']:
                data_C = n.lower()
    return data_A,data_B,data_C


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
    
def metodo(frase):
    sw = stopwords.words('spanish')
    copia = frase
    print('1')
    print(frase)
    frase = frase.lower()
    frase = re.sub('[^A-Za-zñ]+', ' ', frase)
    frase = frase.split()
    print('2')
    print(frase)
    #STOPWORDS
    for w in frase:
        if w in sw:
            #print(word)
            frase.remove(w)
    print('3')
    print(frase)
    
    vpos,vneu,vneg = lowercase()
    # print(vpos,vneu,vneg)
    frase = toke(frase,len(frase),[vpos,vneu,vneg])
    print('4')
    print(frase)
    p= jaccard(frase,[vpos,vneu,vneg])
    cose = np.array([coseno([frase],vpos),coseno([frase],vneu),coseno([frase],vneg)])
    print("coseno:")
    print(cose)
    temp = 1 if  (cose == 0).all() else np.where(cose == np.max(cose))[0][0]
    return {'frase':copia,'jaccard':'MODELO BIO MEDICO' if p == 0 else ( 'ENFOQUE PSICOSOCIAL - COMUNITARIO' if p == 1  else 'ENFOQUE COTIDIANO'),'coseno': 'MODELO BIO MEDICO' if temp == 0 else ( 'ENFOQUE PSICOSOCIAL - COMUNITARIO' if temp == 1  else 'ENFOQUE COTIDIANO')}


def jaccard(v1,v2):
    matrizjacc = []
    for valor in v2:
        a=set(v1)
        b=set(valor)
        union=a.union(b)
        inter=a.intersection(b)
            
        if len(union)==0:
            if len(inter)==0:
                return -1

        similitud=len(inter)/len(union)
        matrizjacc.append(similitud)
    print("jaccard:")
    print(matrizjacc)
    temp = np.array(matrizjacc)
    if  (temp == 0).all():
        return 1
    else:
        return np.where(temp == np.max(temp))[0][0]


#--------------------
#------ COSENO ------
#--------------------
def coseno(documento,vocabulario):
    documento.insert(0,vocabulario)
    documento.insert(2,documento)
    #lista = [[ vocabulario.append(m) for m in h if m not in vocabulario] for h in documento]
    N = len(documento)
    cuenta=[]
    WTF = []
    idf=[]
    idf_tf = []
    for k in range(len(vocabulario)):
        pal = vocabulario[k]
        a1 = [pe(tok.count(pal)) for tok in documento]
        
        df = 0
        for i in a1:
            if i != 0:
                df += 1
        
        op= [e * idf_M(N, df) for e in a1]
        idf_tf.append(op)

    modul = []
    for i in range(len(idf_tf[0])):
        t = 0
        for j in range(len(idf_tf)):
            t += idf_tf[j][i] ** 2
        modul.append(m(t))
    
    logaritmo = [[resM(idf_tf[j][i], modul[i]) for j in range(len(idf_tf))]for i in range(len(idf_tf[0]))]
    matrizT = [[cose(ks, kr) for ks in logaritmo] for kr in logaritmo]
    return np.array(matrizT)[1, 0]


def pe(n):
    if n > 0:
        return round(1 + math.log10(n), 2)
    else:
        return 0

def idf_M(n, df):
    if df > 0:
        return round(math.log10(n/df), 3)
    else:
        return 0

def m(j):
    return math.sqrt(j)


def cose(h1, h2):
    return round(sum(h1[i] * h2[i] for i in range(len(h1))), 2)

def resM(h1,m):
    if m == 0:
        return 0
    else:
        return round(h1/m,3)



def toke(conjunto,index,etiquetas):
    if index == 0:
        return
    else:
        # print("INDEX: "+str(index))
        inicio = 0
        fin = 0
        while fin < len(conjunto)-1:
            fin = inicio + (index-1)
            temp = [conjunto[i] for i in range(inicio,fin+1)]
            temp = " ".join(temp)
            pos = buscar(etiquetas,temp)
            if pos != -1: 
                conjunto[inicio:fin+1] = [temp]
            # print("inicio: "+str(inicio)+ " fin: "+str(fin) + " palabras: "+temp+ " pos: "+str(pos))
            
            inicio += 1
        toke(conjunto,index-1,etiquetas)
    return conjunto
        
def buscar(etiquetas,temp):
    pos = 0
    try:
        pos = etiquetas[0].index(temp)
        return pos
    except:
        pos = -1
    try:
        pos = etiquetas[1].index(temp)
        return pos
    except:
        pos = -1
    try:
        pos = etiquetas[2].index(temp)
        return pos
    except:
        pos = -1
    return pos


