nibbleSubTable = [
    ['0000', '0001'],
    ['0001', '0100'],
    ['0010', '0101'],
    ['0011', '0110'],
    ['0100', '0111'],
    ['0101', '1000'],
    ['0110', '1001'],
    ['0111', '1010'],
    ['1000', '1011'],
    ['1001', '1100'],
    ['1010', '1101'],
    ['1011', '1110'],
    ['1100', '1111'],
    ['1101', '0000'],
    ['1110', '0001'],
    ['1111', '0010']
]
racoon1=[0,0,1,1]
racoon2=[0,0,1,0]
# Printing the table
# for row in nibbleSubTable:
#     print(row)
def nibbleSub(input):
    for i in  range (len(nibbleSubTable)):
        if input == nibbleSubTable[i][0]:
            return nibbleSubTable[i][1]
# generation de cle
def generate_key(k0):
    resultat=bin(int(k0,16))
    char_list = [char for char in resultat]
    converted_list = [int(char) if char.isdigit() else char for char in char_list]
    clean_list=(converted_list[2:])
    w0=clean_list[:4]
    w1=clean_list[4:8]
    w2=clean_list[8:12]
    w3=clean_list[12:16]
    key0=(w0,w1,w2,w3)
    nw3= ''.join(str(bit) for bit in w3)
    nb=[int(char) for char in nibbleSub(nw3)]
    w4=[a^b^c for a,b,c in zip(w0,nb,racoon1)]
    w5=[a^b for a,b in zip(w1,w4)]
    w6=[a^b for a,b in zip(w2,w5)]
    w7=[a^b for a,b in zip(w3,w6)]
    key1=(w4,w5,w6,w7)
    nw7= ''.join(str(bit) for bit in w7)
    nb=[int(char) for char in nibbleSub(nw7)]
    w8=[a^b^c for a,b,c in zip(w4,nb,racoon2)]
    w9=[a^b for a,b in zip(w5,w8)]
    w10=[a^b for a,b in zip(w6,w9)]
    w11=[a^b for a,b in zip(w7,w10)]
    key2=(w8,w9,w10,w11)
    return key0,key1,key2
    

print(generate_key("B2EA"))

# print(type(nibbleSub("0111")))

# def miniAes(key, data): 
