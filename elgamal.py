import random

from params import p
from params import g

def keygen():
    q = (p-1)/2
    sk = random.randint(1,q)
    pk = pow(g, sk, p)
    return pk,sk


def encrypt(pk,m):
    q = (p-1)/2
    r = random.randint(1,q)
        
    c1 = pow(g,r,p)
    
    num = pow(pk,r) * m
    c2 = pow(num, 1, p)
    
    return [c1,c2]


def decrypt(sk,c):
    nominator = c[1]
    
    denominator = pow(c[0], sk)
    
    num = nominator/denominator
    
    m = pow(num, 1, p)
    
    return m
