# Python pour l'algorithme cryptographique asymétrique RSA.
# Pour la démonstration, les valeurs sont
# relativement petites par rapport à une application pratique
import math


def pgcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp


p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)

while (e < phi):
    # e doit être premier avec phi et
    # plus petit que phi.
    if(pgcd(e, phi) == 1):
        break
    else:
        e = e+1

# Clé privée (d représente le décryptage)
# choisir d de manière à ce qu'elle satisfasse
# d*e = 1 + k * indicatrice

k = 2
d = (1 + (k*phi))/e

# Message à chiffrer
msg = 12.0

print("==> Données du message = ", msg)

# Chiffrement c = (msg ^ e) % n
c = pow(msg, e)
c = math.fmod(c, n)
print("==> Données chiffrées = ", c)

# Déchiffrement m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("==> Message original envoyé = ", m)

