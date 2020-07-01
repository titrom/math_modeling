print("____________________________laba_3_osnov_2_a________________________")
from math import tan, cos, pi
h = 100
A = pi
B = pi / 6
from astro_constants import acceleration_of_gravity_ears as g
float(a) = g * h * (tan(B))**2
b = 2 * cos (A)**2 * ( 1 - tan(B) * tan(A) )
c = a / b
v = c**0.5
print(" v = ", v)
print()

print("____________________________laba_3_osnov_2_b________________________")
from math import  pi
from astro_constants import constant_planka, chislo_elera, constant_boltsmana
t = 200
e = 300
n = 2/pi * constant_planka / ( constant_boltsmana * t )**(3/2) * chislo_elera**(-e / (constant_boltsmana * t)) * e**(t/2)
print("n = ", n)