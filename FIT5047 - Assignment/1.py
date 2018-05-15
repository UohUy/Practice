#!/usr/bin/env
# -*-coding:utf-8-*-
import math
import random
import time

sin = math.sin
pi = math.pi
exp = math.exp
T_START = 1000
T_MIN = pow(10, -7)
delta = 0.0001


class Task2:
    def __init__(self):
        self.p = 0
        self.t = T_START
        self.t_min = T_MIN
        self.result = 0

    @staticmethod
    def random_y():
        return random.choice([1, 0, -1])

    @staticmethod
    def random_x():
        return random.randint(0, 10000001) / 10000000.0

    @staticmethod
    def random_variable():
        return random.uniform(0, 10000001) / 5000000.0 - 1

    @staticmethod
    def func_2a(u):
        return u * sin(1 / (0.01 + u ** 2)) + u ** 3 * sin(1 / (0.001 + u ** 4))

    @staticmethod
    def func_2b(u, v):
        return u * v ** 2 * sin(v / (0.01 + u ** 2)) + u ** 3 * v ** 2 * sin(
            v ** 3 / (0.001 + u ** 4))

    @staticmethod
    def func_2c(u, v, w):
        return (u * v ** 2 + sin(pi * w)) * sin(v / (0.01 + u ** 2)) * sin(pi * w / 2) + u ** 3 * v ** 2 * w * sin(
            v ** 3 / (0.001 * sin(pi * w / 2) ** 2 + u ** 4 + (w - 1) ** 2))

    @staticmethod
    def func_2d(u, v, w, y):
        return Task2.func_2c(u, v, w, ) * y

    def update_p(self, new_result):
        diff = abs(new_result - self.result)
        t = self.t

        # The boundary of math.exp() function is approximately equals to 709
        if diff / t > 709:
            self.p = 1 / (1 + exp(709))
        else:
            self.p = 1 / (1 + exp(diff / t))

    def get_2a_result(self):
        i = 0
        start = time.clock()
        while self.t > self.t_min:
            i += 1
            x = self.random_x()
            u = self.random_variable()
            current_result = Task2.func_2a(u)
            if current_result > self.result:
                self.result = current_result
            else:
                self.update_p(current_result)
                if 0 <= x <= self.p:
                    self.result = current_result
            self.t = self.t * (1 - delta)
            # print("T, u and z:", self.t, u, current_result)
        end = time.clock()
        print("Final result is:", self.result)
        print('%d times simulation. Cost %f second' % (i, (end - start)))

    def get_2b_result(self):
        i = 0
        start = time.clock()
        while self.t > self.t_min:
            i += 1
            x = self.random_x()
            u = self.random_variable()
            v = self.random_variable()
            current_result = Task2.func_2b(u, v)
            if current_result > self.result:
                self.result = current_result
            else:
                self.update_p(current_result)
                if 0 <= x <= self.p:
                    self.result = current_result
            self.t = self.t * (1 - delta)
            # print("T, u, v and z:", self.t, u, v, current_result)
        end = time.clock()
        print("Final result is:", self.result)
        print(i, "times simulation. Cost %f second" % (end - start))

    def get_2c_result(self):
        i = 0
        start = time.clock()
        while self.t > self.t_min:
            i += 1
            u = self.random_variable()
            v = self.random_variable()
            w = self.random_variable()
            current_result = Task2.func_2c(u, v, w)
            if current_result > self.result:
                self.result = current_result
            else:
                x = self.random_x()
                self.update_p(current_result)
                if 0 <= x <= self.p:
                    self.result = current_result
            self.t = self.t * (1 - delta)
            # print("T, u, v, w and z:", self.t, u, v, w, current_result)
        end = time.clock()
        print("Final result is:", self.result)
        print('%d times simulation. Cost %f second' % (i, (end - start)))

    def get_2d_result(self):
        i = 0
        start = time.clock()
        while self.t > self.t_min:
            i += 1
            u = self.random_variable()
            v = self.random_variable()
            w = self.random_variable()
            y = self.random_y()
            current_result = Task2.func_2d(u, v, w, y)
            if current_result > self.result:
                self.result = current_result
            else:
                x = self.random_x()
                self.update_p(current_result)
                if 0 <= x <= self.p:
                    self.result = current_result
            self.t = self.t * (1 - delta)
            # print("T, u, v ,w and z:", self.t, u, v, w, current_result)
        end = time.clock()
        print("Final result is:", self.result)
        print('%d times simulation. Cost %f second' % (i, (end - start)))
        # TODO add y


def run():
    while True:
        print("---------Task 2---------")
        print("1. 2a")
        print("2. 2b")
        print("3. 2c")
        print("4. 2d")
        print("5. Exit")
        print("Please input your choice:")
        choice = input()
        task2 = Task2()
        if choice == '5':
            break
        elif choice == '1':
            task2.get_2a_result()
        elif choice == '2':
            task2.get_2b_result()
        elif choice == '3':
            task2.get_2c_result()
        elif choice == '4':
            print()  # TODO Choose y
            task2.get_2d_result()


if __name__ == '__main__':
    run()
