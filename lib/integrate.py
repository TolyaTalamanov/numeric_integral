import numpy as np 

class Integrate:

    def __init__(self, func, count_points = 1000):
        self._func = func
        self._count_points = count_points

    def squad(self, limits):
            step = (limits[1] - limits[0]) / self._count_points 
            area = 0
            for x in np.arange(limits[0], limits[1], step):
                area += step * self._func(x + 0.5 * step) 
            return area				

    def trapeze(self, limits):
            step = (limits[1] - limits[0]) / self._count_points
            area = 0
            for x in np.arange(limits[0], limits[1], step):
                area += step * (self._func(x) + self._func(x + step)) / 2
            return area

    def simpson(self, limits):
            step = (limits[1] - limits[0]) / self._count_points
            area = 0
            for x in np.arange(limits[0], limits[1], step):
                area += step / 6 * (self._func(x) + 4 * self._func(x + 0.5 * step) +
                        self._func(x + step))
            return area		

