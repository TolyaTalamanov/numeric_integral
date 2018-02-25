import lib.integrate as integrate 
from math import sin, cos

def integrate_sin(limits):
    return -cos(limits[1]) + cos(limits[0])

sinx     = lambda x: sin(x)
limits   = list(map(int, (input("Введите пределы интегрирования через пробел : ").split(' '))))
integral = integrate.Integrate(sinx)


print("Точное значение      = {0}\n".format(integrate_sin(limits)))

print("Метод трапеций = {0}\nГлобальная погрешность      = {1}\n".format(integral.trapeze(limits),
                             abs(integral.trapeze(limits) - integrate_sin(limits))))

print("Метод центральных прямоугольников    = {0}\nГлобальная погрешность      = {1}\n".format(integral.squad(limits),
                             abs(integral.squad(limits) - integrate_sin(limits))))

print("Метод Симпсона = {0}\nГлобальная погрешность      = {1}\n".format(integral.simpson(limits),
                             abs(integral.simpson(limits) - integrate_sin(limits))))

print("Метода Гаусса   = {0}\nГлобальная погрешность      = {1}\n".format(integral.gauss(limits),
                             abs(integral.gauss(limits) - integrate_sin(limits))))

print("Метод Монте-Карло = {0}\nГлобальная погрешность  = {1}\n".format(integral.montecarlo(limits),
                             abs(integral.montecarlo(limits) - integrate_sin(limits))))
