def recherche_SubByte(valeur_binaire):
    SubByte = [
        ['0000', '0001',
        '0010', '0011',
        '0100', '0101',
        '0110', '0111',
        '1000', '1001',
        '1010', '1011',
        '1100', '1101',
        '1110', '1111'],
        ['1110', '0100', 
         '1101', '0001', 
         '0010', '1111',
        '1011', '1000',
        '0011', '1010', 
        '0110', '1100',
        '0101', '1001', 
        '0000', '0111']
    ]

    index_colonne = SubByte[0].index(valeur_binaire)
    valeur_resultat = SubByte[1][index_colonne]
    
    return valeur_resultat
#la fonction recon 
def recon(x):
    if x == 1:
        return '0001'
    elif x == 2:
        return '0010'
    else:
        return 'Erreur: x doit être 1 ou 2 pour cette fonction'
def generationkeys(key0):
    if len(key0) != 16:
        return "Erreur: La clé doit être de 16 bits"
    
    w0 = key0[0:4]
    w1 = key0[4:8]
    w2 = key0[8:12]
    w3 = key0[12:16]
    
    w4 = int(w0, 2) ^ int(recherche_SubByte(w3), 2) ^ int(recon(1), 2)
    w5 = int(w1, 2) ^ w4
    w6 = int(w2, 2) ^ w5
    w7 = int(w3, 2) ^ w6
   
    w8 = w4 ^ int(recherche_SubByte(bin(w7)[2:].zfill(4)), 2) ^ int(recon(2), 2)
    w9 = w5 ^ w8
    w10 = w6 ^ w9
    w11 = w7 ^ w10

    k = w0 + w1 + w2 + w3
    k1 = format(w4, '04b') + format(w5, '04b') + format(w6, '04b') + format(w7, '04b')
    k2 = format(w8, '04b') + format(w9, '04b') + format(w10, '04b') + format(w11, '04b')
    return  k1, k2

key = "1100001111110000"
k1, k2 = generationkeys(key)
print("==> k1:", k1)
print("==> k2:", k2)
def SubByteetShiftRows(texte):
    p0 = texte[0:4]
    p1 = texte[4:8]
    p2 = texte[8:12]
    p3 = texte[12:16]
    
    b0=recherche_SubByte(p0)
    b1=recherche_SubByte(p1)
    b2=recherche_SubByte(p2)
    b3=recherche_SubByte(p3)
    
    c0=b0
    c1=b3
    c2=b2
    c3=b1
    return c0,c1,c2,c3

texte ='1001110001100011'
c0,c1,c2,c3 = SubByteetShiftRows(texte)
print ("==> c0 :",c0)
print ("==> c1 :",c1)
print ("==> c2 :",c2)
print ("==> c3 :",c3)
def MixColumns(texte):
    c0, c1, c2, c3 = SubByteetShiftRows(texte)  
    matrix = [['0011', '0010'], ['0010', '0011']]
    mat1 = [[c0], [c1]]
    mat2 = [[c2], [c3]]


    d0= bin ((int(matrix[0][0],2) & int (mat1[0][0],2))  ^  (int(matrix[0][1],2) & int (mat1[1][0],2)))[2:].zfill(4)
    d1= bin ((int(matrix[1][0],2) & int (mat1[0][0],2))  ^  (int(matrix[1][1],2) & int (mat1[1][0],2)))[2:].zfill(4)
    d2= bin ((int(matrix[0][0],2) & int (mat2[0][0],2))  ^  (int(matrix[0][1],2) & int (mat2[1][0],2)))[2:].zfill(4)
    d3= bin ((int(matrix[1][0],2) & int (mat2[0][0],2))  ^  (int(matrix[1][1],2) & int (mat2[1][0],2)))[2:].zfill(4)
   
    return d0,d1,d2,d3
MixColumns('1001110001100011')


def MiniAES(texte, key0):
    k1, k2 = generationkeys(key0)
    d0, d1, d2, d3 = MixColumns(texte)
    # 1st round
    k00 = k1[0:4]
    k11 = k1[4:8]
    k22 = k1[8:12]
    k33 = k1[12:16]

    e0 = bin(int(k00, 2) ^ int(d0, 2))[2:].zfill(4)
    e1 = bin(int(k11, 2) ^ int(d1, 2))[2:].zfill(4)
    e2 = bin(int(k22, 2) ^ int(d2, 2))[2:].zfill(4)
    e3 = bin(int(k33, 2) ^ int(d3, 2))[2:].zfill(4)
    texte1 = e0 + e1 + e2 + e3
 #Add round key 
    # 2nd round
    d00, d11, d22, d33 = MixColumns(texte1)
    k000 = k2[0:4]
    k111 = k2[4:8]
    k222 = k2[8:12]
    k333 = k2[12:16]
    
    e00 = bin(int(k000, 2) ^ int(d00, 2))[2:].zfill(4)
    e11 = bin(int(k111, 2) ^ int(d11, 2))[2:].zfill(4)
    e22 = bin(int(k222, 2) ^ int(d22, 2))[2:].zfill(4)
    e33 = bin(int(k333, 2) ^ int(d33, 2))[2:].zfill(4)
    
    message_chiffre = e00 + e11 + e22 +e33
    
    return  message_chiffre

mssg = MiniAES("1001110001100011", '1100001111110000')
print ("==> Le message chiffré par l'algorithme AES est :",mssg)
