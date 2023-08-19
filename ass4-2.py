# -*- coding: utf-8 -*-
"""
assignment 4-2
"""

"""
4-2(i)
"""
import sys
import traceback


class GaussElimination:
    def __init__(self):
      self.a = [
          [ 1, -2,  1,  2],
          [ 2,  3,  4,  3],
          [ 3,  2,  1,  4]
      ]
      self.n = len(self.a)

    def exec(self):
        """ Execution """
        try:
            self.__display_equations()
            for k in range(self.n - 1):
                for i in range(k + 1, self.n):
                    d = self.a[i][k] / self.a[k][k]
                    for j in range(k + 1, self.n + 1):
                        self.a[i][j] -= self.a[k][j] * d
            for i in range(self.n - 1, -1, -1):
                d = self.a[i][self.n]
                for j in range(i + 1, self.n):
                    d -= self.a[i][j] * self.a[j][self.n]
                self.a[i][self.n] = d / self.a[i][i]
            self.__display_answers()
        except Exception as e:
            raise

    def __display_equations(self):
        """ Display of source equations """
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        """ Display of answer """
        try:
            for k in range(self.n):
                print("x{:d} = {:f}".format(k + 1, self.a[k][self.n]))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = GaussElimination()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
        
"""
4-2(ii)
"""
import sys
import traceback


class GaussElimination:
    def __init__(self):
      self.a = [
          [     1,  2000,  3000,  5001],
          [ -1000,  3712,  4623,  7335],
          [ -2000,  1072,  5643,  4715]
      ]
      self.n = len(self.a)

    def exec(self):
        """ Execution """
        try:
            self.__display_equations()
            for k in range(self.n - 1):
                for i in range(k + 1, self.n):
                    d = self.a[i][k] / self.a[k][k]
                    for j in range(k + 1, self.n + 1):
                        self.a[i][j] -= self.a[k][j] * d
            for i in range(self.n - 1, -1, -1):
                d = self.a[i][self.n]
                for j in range(i + 1, self.n):
                    d -= self.a[i][j] * self.a[j][self.n]
                self.a[i][self.n] = d / self.a[i][i]
            self.__display_answers()
        except Exception as e:
            raise

    def __display_equations(self):
        """ Display of source equations """
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        """ Display of answer """
        try:
            for k in range(self.n):
                print("x{:d} = {:f}".format(k + 1, self.a[k][self.n]))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = GaussElimination()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit()     
    
        
"""
4-2(iii)
"""
import sys
import traceback

ax = 2
class GaussElimination:
    def __init__(self):
      self.a = [
          [ ax,  1,  1+ax*ax-ax], #両辺に正の定数をかける
          [ 1,  1,  1]
      ]
      self.n = len(self.a)

    def exec(self):
        """ Execution """
        try:
            self.__display_equations()
            for k in range(self.n - 1):
                for i in range(k + 1, self.n):
                    d = self.a[i][k] / self.a[k][k]
                    for j in range(k + 1, self.n + 1):
                        self.a[i][j] -= self.a[k][j] * d
            for i in range(self.n - 1, -1, -1):
                d = self.a[i][self.n]
                for j in range(i + 1, self.n):
                    d -= self.a[i][j] * self.a[j][self.n]
                self.a[i][self.n] = d / self.a[i][i]
            self.__display_answers()
        except Exception as e:
            raise

    def __display_equations(self):
        """ Display of source equations """
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        """ Display of answer """
        try:
            for k in range(self.n):
                print("x{:d} = {:f}".format(k + 1, self.a[k][self.n]))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = GaussElimination()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit()

        

#(iii)2
ax = 10**10
class GaussElimination:
    def __init__(self):
      self.a = [
          [ ax,  1,  1+ax*ax-ax], #両辺に正の定数をかける
          [ 1,  1,  1]
      ]
      self.n = len(self.a)

    def exec(self):
        """ Execution """
        try:
            self.__display_equations()
            for k in range(self.n - 1):
                for i in range(k + 1, self.n):
                    d = self.a[i][k] / self.a[k][k]
                    for j in range(k + 1, self.n + 1):
                        self.a[i][j] -= self.a[k][j] * d
            for i in range(self.n - 1, -1, -1):
                d = self.a[i][self.n]
                for j in range(i + 1, self.n):
                    d -= self.a[i][j] * self.a[j][self.n]
                self.a[i][self.n] = d / self.a[i][i]
            self.__display_answers()
        except Exception as e:
            raise

    def __display_equations(self):
        """ Display of source equations """
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        """ Display of answer """
        try:
            for k in range(self.n):
                print("x{:d} = {:f}".format(k + 1, self.a[k][self.n]))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = GaussElimination()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit()
        

#(iii)3
ax = 10**15
class GaussElimination:
    def __init__(self):
      self.a = [
          [ ax,  1,  1+ax*ax-ax], #両辺に正の定数をかける
          [ 1,  1,  1]
      ]
      self.n = len(self.a)

    def exec(self):
        """ Execution """
        try:
            self.__display_equations()
            for k in range(self.n - 1):
                for i in range(k + 1, self.n):
                    d = self.a[i][k] / self.a[k][k]
                    for j in range(k + 1, self.n + 1):
                        self.a[i][j] -= self.a[k][j] * d
            for i in range(self.n - 1, -1, -1):
                d = self.a[i][self.n]
                for j in range(i + 1, self.n):
                    d -= self.a[i][j] * self.a[j][self.n]
                self.a[i][self.n] = d / self.a[i][i]
            self.__display_answers()
        except Exception as e:
            raise

    def __display_equations(self):
        """ Display of source equations """
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        """ Display of answer """
        try:
            for k in range(self.n):
                print("x{:d} = {:f}".format(k + 1, self.a[k][self.n]))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = GaussElimination()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit()



#4
ax = -10**15
class GaussElimination:
    def __init__(self):
      self.a = [
          [ ax,  1,  1+ax*ax-ax], #両辺に正の定数をかける
          [ 1,  1,  1]
      ]
      self.n = len(self.a)

    def exec(self):
        """ Execution """
        try:
            self.__display_equations()
            for k in range(self.n - 1):
                for i in range(k + 1, self.n):
                    d = self.a[i][k] / self.a[k][k]
                    for j in range(k + 1, self.n + 1):
                        self.a[i][j] -= self.a[k][j] * d
            for i in range(self.n - 1, -1, -1):
                d = self.a[i][self.n]
                for j in range(i + 1, self.n):
                    d -= self.a[i][j] * self.a[j][self.n]
                self.a[i][self.n] = d / self.a[i][i]
            self.__display_answers()
        except Exception as e:
            raise

    def __display_equations(self):
        """ Display of source equations """
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        """ Display of answer """
        try:
            for k in range(self.n):
                print("x{:d} = {:f}".format(k + 1, self.a[k][self.n]))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = GaussElimination()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit()
        



#5

ax = 10**20
class GaussElimination:
    def __init__(self):
      self.a = [
          [ ax,  1,  1+ax*ax-ax], #両辺に正の定数をかける
          [ 1,  1,  1]
      ]
      self.n = len(self.a)

    def exec(self):
        """ Execution """
        try:
            self.__display_equations()
            for k in range(self.n - 1):
                for i in range(k + 1, self.n):
                    d = self.a[i][k] / self.a[k][k]
                    for j in range(k + 1, self.n + 1):
                        self.a[i][j] -= self.a[k][j] * d
            for i in range(self.n - 1, -1, -1):
                d = self.a[i][self.n]
                for j in range(i + 1, self.n):
                    d -= self.a[i][j] * self.a[j][self.n]
                self.a[i][self.n] = d / self.a[i][i]
            self.__display_answers()
        except Exception as e:
            raise

    def __display_equations(self):
        """ Display of source equations """
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        """ Display of answer """
        try:
            for k in range(self.n):
                print("x{:d} = {:f}".format(k + 1, self.a[k][self.n]))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = GaussElimination()
        obj.exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit()        
        
        