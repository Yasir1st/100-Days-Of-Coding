import random
import string

def line():
    print("="*100)

def lineMini():
    print("-"*100)

def random_string(panjang:int) -> str:
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_string