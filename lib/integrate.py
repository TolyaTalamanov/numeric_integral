import numpy as np 

class Integrate:

    def __init__(self, func, count_points = 1000):
        self._func = func
        self._count_points = count_points

        self._A = [ [ 2 ],
        [ 1, 1 ],
        [ 0.5555555556,0.8888888888,0.5555555556 ],
        [ 0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451 ],
        [ 0.2369268851, 0.4786286705, 0.5688888888,  0.4786286705,0.2369268851 ],
        [ 0.1713244924, 0.3607615730, 0.4679139346, 0.4679139346, 0.3607615730, 0.1713244924 ] ]
         
        self._T = [ [ 0 ],
        [ -0.5773502692, 0.5773502692 ],
        [ -0.7745966692, 0.0000000000, 0.7745966692 ],
        [ -0.8611363115, -0.3399810436, 0.3399810436, 0.8611363115 ],
        [ -0.9061798459, -0.5384693101, 0.0000000000, 0.5384693101, 0.9061798459 ],
        [ -0.9324695142, -0.6612093864, -0.2386191861, 0.2386191861, 0.6612093864, 0.9324695142 ] ]


    def squad(self, limits):
            step = (limits[1] - limits[0]) / self._count_points 
            sum = 0
            for x in np.arange(limits[0], limits[1], step):
                sum += step * self._func(x + 0.5 * step) 
            return sum				

    def trapeze(self, limits):
            step = (limits[1] - limits[0]) / self._count_points
            sum = 0
            for x in np.arange(limits[0], limits[1], step):
                sum += step * (self._func(x) + self._func(x + step)) / 2
            return sum

    def simpson(self, limits):
            step = (limits[1] - limits[0]) / self._count_points
            sum = 0
            for x in np.arange(limits[0], limits[1], step):
                sum += step / 6 * (self._func(x) + 4 * self._func(x + 0.5 * step) +
                        self._func(x + step))
            return sum		

    def gauss(self, limits, nodes = 4):
            h = (limits[1] - limits[0]) / 2
            sum = 0
            for i in range(nodes):
                sum += self._A[nodes - 1][i] * self._func((limits[0] + limits[1]) / 2 +
                        ((limits[1] - limits[0]) / 2) * self._T[nodes - 1][i])
            return sum * h
