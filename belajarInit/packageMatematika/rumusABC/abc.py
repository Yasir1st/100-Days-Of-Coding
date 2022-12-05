'''Rumus ABC'''
def a_b_c(a,b,c):
    hasilPlus = ((-1*b)+((b**2)-4*a*c)**(1/2))/2*a
    hasilMinus = ((-1*b)-((b**2)-4*a*c)**(1/2))/2*a
    hasil = f"x1 = {hasilPlus} dan x2 = {hasilMinus}"
    return hasil