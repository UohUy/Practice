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

    def get_2a_result(self, u=random_variable()):
        i = 0
        start = time.clock()
        self.result = self.func_2a(u)
        while self.t > self.t_min:
            print("T, u and z:", self.t, u, self.result)
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
        end = time.clock()
        print("Final result is:", self.result)
        print('%d times simulation. Cost %f second' % (i, (end - start)))

    def get_2b_result(self, u=random_variable(), v=random_variable()):
        i = 0
        start = time.clock()
        self.result = self.func_2b(u, v)
        while self.t > self.t_min:
            print("T, u, v and z:", self.t, u, v, self.result)
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
        end = time.clock()
        print("Final result is:", self.result)
        print(i, "times simulation. Cost %f second" % (end - start))

    def get_2c_result(self, u=random_variable(), v=random_variable(), w=random_variable()):
        i = 0
        start = time.clock()
        self.result = self.func_2c(u, v, w)
        while self.t > self.t_min:
            print("T, u, v, w and z:", self.t, u, v, w, self.result)
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
        end = time.clock()
        print("Final result is:", self.result)
        print('%d times simulation. Cost %f second' % (i, (end - start)))

    def get_2d_result(self, u=random_variable(), v=random_variable(), w=random_variable(), y=random_y()):
        i = 0
        start = time.clock()
        self.result = self.func_2d(u, v, w, y)
        while self.t > self.t_min:
            print("T, u, v ,w and z:", self.t, u, v, w, self.result)
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
        end = time.clock()
        print("Final result is:", self.result)
        print('%d times simulation. Cost %f second' % (i, (end - start)))


def display_2a_menu():
    while True:
        print("---------2a---------")
        print("1. Variables start as 0")
        print("2. Variables start randomly")
        print("3. Input variables")
        print("4. Go back to previous page")
        task2 = Task2()
        choice = input()
        if choice == '1':
            task2.get_2a_result(0)
        if choice == '2':
            task2.get_2a_result()
        if choice == '3':
            print('Please input u: ')
            u = input()
            task2.get_2a_result(u)


def display_2b_menu():
    while True:
        print("---------2a---------")
        print("1. Variables start as 0")
        print("2. Variables start randomly")
        print("3. Input variables")
        print("4. Go back to previous page")
        task2 = Task2()
        choice = input()
        if choice == '1':
            task2.get_2b_result(0, 0)
        if choice == '2':
            task2.get_2b_result()
        if choice == '3':
            print('Please input u, v: ')
            variables = input()
            u, v = variables.split(',')
            task2.get_2b_result(u, v)


def display_2c_menu():
    while True:
        print("---------2a---------")
        print("1. Variables start as 0")
        print("2. Variables start randomly")
        print("3. Input variables")
        print("4. Go back to previous page")
        task2 = Task2()
        choice = input()
        if choice == '1':
            task2.get_2c_result(0, 0, 0)
        if choice == '2':
            task2.get_2c_result()
        if choice == '3':
            print('Please input u, v, w: ')
            variables = input()
            u, v, w = variables.split(',')
            task2.get_2c_result(u, v, w)


def display_2d_menu():
    while True:
        print("---------2a---------")
        print("1. Variables start as 0")
        print("2. Variables start randomly")
        print("3. Input variables")
        print("4. Go back to previous page")
        task2 = Task2()
        choice = input()
        if choice == '1':
            task2.get_2d_result(0, 0, 0, 0)
        if choice == '2':
            task2.get_2d_result()
        if choice == '3':
            print('Please input u, v, w: ')
            variables = input()
            u, v, w, y = variables.split(',')
            task2.get_2d_result(u, v, w, y)

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
        if choice == '5':
            break
        elif choice == '1':
            display_2a_menu()
        elif choice == '2':
            display_2b_menu()
        elif choice == '3':
            display_2c_menu()
        elif choice == '4':
            display_2d_menu()


if __name__ == '__main__':
    run()
