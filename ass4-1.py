# -*- coding: utf-8 -*-
"""
assignment 4-1
"""
import sys
import traceback

class GaussElimination:
    def __init__(self):
      self.a = [
          [ 1,  1,  1,  1,  1],
          [ 3,  1,  1, -1,  3],
          [ 1,  1, -1,  1,  1],
          [ 1, -1,  1,  2,  5]
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
4-1'

import sys
import traceback


class GaussElimination:
    def __init__(self):
      self.a = [
          [ 1000000,  1000000,  1000000,  1000000,  1000000],
          [ 30,  10,  10, -10,  30],
          [ 1,  1, -1,  1,  1],
          [ 1, -1,  1,  2,  5]
      ]
      self.n = len(self.a)

    def exec(self):
        #Execution
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
        # Display of source equations
        try:
            for i in range(self.n):
                for j in range(self.n):
                    print("{:+d}x{:d} ".format(self.a[i][j], j + 1), end="")
                print("= {:+d}".format(self.a[i][self.n]))
        except Exception as e:
            raise

    def __display_answers(self):
        # Display of answer 
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
        