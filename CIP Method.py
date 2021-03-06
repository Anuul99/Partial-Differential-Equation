# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XI4xsPi5s55D7vdibDPsui9XRmlDfIVo
"""

import numpy as np
import matplotlib.pyplot as plt
# Initial Values
dx = 1.0
C = 0.1 
u = 1.0 
dt = 0.1
# Time span and X
x = np.arange(0, 100+dx, dx)
t = np.arange(0, 1000+dt, dt)
# Assigning f(0,x)
f = np.zeros(x.shape[0])
f[40:60] = 1

fx=np.copy(f)

g = (np.roll(fx,-1)-np.roll(fx,1))/(2*dx)

for iter in t:
    a = -2*(np.roll(fx,int(np.sign(u)),0)-fx)/((-dx*np.sign(u))**3)+(g+np.roll(g,int(np.sign(u))))/((-dx*np.sign(u))**2)
    b = -3*(fx-np.roll(fx,int(np.sign(u)),0))/((-dx*np.sign(u))**2)-(2*g+np.roll(g,int(np.sign(u))))/(-dx*np.sign(u))
    fx = a*(-C*dx)**3+b*(-C*dx)**2+g*(-C*dx)+fx
    g = 3*a*(-u*C*dx)**2+2*b*(-C*dx)+g
    if iter==10:
        plt.plot(x,fx, label= f'When t is {iter}')
        plt.legend()
    if iter==200:
        plt.plot(x,fx, label= f'When t is {iter}')
        plt.legend()
    if iter==400:
        plt.plot(x,fx, label= f'When t is {iter}')
        plt.legend()
    if iter==600:
        plt.plot(x,fx, label= f'When t is {iter}')
        plt.legend()