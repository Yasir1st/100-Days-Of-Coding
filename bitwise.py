import os
os.system("cls")

def line():
    print("="*40)

a = 60
b = 13

bin_a = bin(a)
bin_b = bin(b)

line()
print(f"a : {a}")
print(f"b : {b}")
print(f"Binery a : {bin_a}")
print(f"Binery b : {bin_b}")
line()

# Operator AND(&)
print(f"a & b : {a & b}")
print(f"a & b : {bin(a & b)}")
line()
# Operator OR(|)
print(f"a | b : {a | b}")
print(f"a | b : {bin(a | b)}")
line()
# Operator XOR(^)
print(f"a ^ b : {a ^ b}")
print(f"a ^ b : {bin(a ^ b)}")
line()
# Operator NOT(~)
print(f"~a : {~a}")
print(f"~a : {bin(~a)}")
print(f"~b : {~b}")
print(f"~b : {bin(~b)}")
line()
# Operasi shift left (tukar posisi biner)(<<)
print(f"a << b : {a << b}")
print(f"a << b : {bin(a << b)}")
line()
# Operasi shift right (tukar posisi biner)(>>)
print(f"a >> b : {a >> b}")
print(f"a >> b : {bin(a >> b)}")
line()