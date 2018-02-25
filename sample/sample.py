import lib.integrate as integrate 
from math import sin, cos, exp

def integrate_exp(limits):
    return exp(limits[1]) - exp(limits[0])

expx     = lambda x: exp(x)
limits   = list(map(int, (input("Введите пределы интегрирования через пробел : ").split(' '))))
integral = integrate.Integrate(expx)


print("Точное значение      = {0}\n".format(integrate_exp(limits)))

print("Метод трапеций = {0}\nГлобальная погрешность      = {1}\n".format(integral.trapeze(limits),
                             abs(integral.trapeze(limits) - integrate_exp(limits))))

print("Метод центральных прямоугольников    = {0}\nГлобальная погрешность      = {1}\n".format(integral.squad(limits),
                             abs(integral.squad(limits) - integrate_exp(limits))))

print("Метод Симпсона = {0}\nГлобальная погрешность      = {1}\n".format(integral.simpson(limits),
                             abs(integral.simpson(limits) - integrate_exp(limits))))

print("Метода Гаусса   = {0}\nГлобальная погрешность      = {1}\n".format(integral.gauss(limits),
                             abs(integral.gauss(limits) - integrate_exp(limits))))

print("Метод Монте-Карло = {0}\nГлобальная погрешность  = {1}\n".format(integral.montecarlo(limits),
                             abs(integral.montecarlo(limits) - integrate_exp(limits))))
