from math import * #old import * from math
print("Ruudu karakteristikud")
a=int(input("Sisesta ruudu külje pikkus => ")) #added int and changed ' on "
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #changed '' on "
di=a*sqrt(2) #math.sqr(2) change to sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #deleted ")"
b=int(input("Sisesta ristküliku 1. külje pikkus => ")) #added int
c=int(input("Sisesta ristküliku 2. külje pikkus => ")) #added int
S=b*c
print("Ristküliku pindala", S) #added "
P=2*(b+c) #added *
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) #deleted math and added * where it was needed
print("Ristküliku diagonaal", round(di,1)) #added ")" and added (di,1) so we can see 1 mark after ,
print()
print("Ringi karakteristikud")
r=int(input("Sisesta ringi raadiusi pikkus => ")) #added int and changed '' on "
d=2*r #added *
print("Ringi läbimõõt", d) #added , before d
S=pi*(r**2) #added extra * deleted() after pi
print("Ringi pindala", round(S,2)) #added (S,2) so we can see 2 marks after ,
C=2*pi*r #added * between 2 & deleted() after pi
print("Ringjoone pikkus", round(C,2)) #added ) and added (S,2) so we can see 2 marks after ,