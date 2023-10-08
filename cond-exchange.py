A = int(input("donnez la valeur de A:"))
B = int(input("donnez la valeur de B:"))
if A*B>0 :
A,B=B,A
else:
C = A + B
D = A * B
A = C
B = D
print("la nouvelle valeur de A est:",A)
print("la nouvelle valeur de B est:",B)
