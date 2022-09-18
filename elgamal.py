import random

from params import p
from params import g

def keygen():
    q = (p-1)/2
    sk = random.randint(1,q)
    pk = pow(g, sk, p)
    return pk,sk
