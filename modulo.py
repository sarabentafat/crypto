def modulo(number,puissance,N):
    binary = bin(puissance)
    char_list = [char for char in binary]
    converted_list = [int(char) if char.isdigit() else char for char in char_list]
    clean_list=(converted_list[2:])
    reversed_list = list(reversed(clean_list))
    lista=[number]
    nbr=number
    for i in range(len(reversed_list)) :
        nbr=(nbr**2 )% N
        lista.append(nbr)

    nlista=[]
    for i in range(len(reversed_list)):
        if reversed_list[i]==1 :
            nlista.append(lista[i])
    s=1
    for i in range(len(nlista)):
        s=s*nlista[i]
    return s%N
print("*"*100)
number = input("==> Enter un nombre")
puissance = input("==> Enter le puissance ")
N= input("==> Enter le N")
print("*"*100)
print("==> Le resultat de modulo est:", modulo(int(number),int(puissance),int(N)))

