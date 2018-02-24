import lib.integrate as integrate 
from math import sin, cos

def integrate_sin(limits):
    return -cos(limits[1]) + cos(limits[0])

sinx     = lambda x: sin(x)
limits   = list(map(int, (input("Enter limits : ").split(' '))))
integral = integrate.Integrate(sinx)


print("exact meaning     = {0}\n".format(integrate_sin(limits)))

print("integrate trapeze = {0}\nglobal error      = {1}\n".format(integral.trapeze(limits),
                             abs(integral.trapeze(limits) - integrate_sin(limits))))

print("integrate squad   = {0}\nglobal error      = {1}\n".format(integral.squad(limits),
                             abs(integral.squad(limits) - integrate_sin(limits))))

print("integrate simpson = {0}\nglobal error      = {1}\n".format(integral.simpson(limits),
                             abs(integral.simpson(limits) - integrate_sin(limits))))

print("integrate gauss   = {0}\nglobal error      = {1}\n".format(integral.gauss(limits),
                             abs(integral.gauss(limits) - integrate_sin(limits))))

print("integrate montecarlo = {0}\nglobal error  = {1}\n".format(integral.montecarlo(limits),
                             abs(integral.montecarlo(limits) - integrate_sin(limits))))
