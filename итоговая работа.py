# -*- coding: utf-8 -*-

# -- Sheet --

from sympy import *
from sympy.plotting import plot

x = Symbol("x")
#на уроке
#f = 5 * x ** 2 + 10 * x - 30
#f = (x * (x + 2)) / (2 * x - 1)

f=-18*x**3+5 * x ** 2 + 10 * x - 30
#f = 2*x**3+2*x**2-18*x-18
#f = (x**2+3)/(3*(x+1))
#f= -12*x**4*sin(cos(x))-18*x**3+5*x**2+1*x-30
#f=-3*x**4-16*x**3+24*x**2-11
f

#Определить корни
#Нули функции

solveset(f, x, Reals).evalf(2)

#Найти интервалы возростания и убывания функции
#

f_diff = [-oo, oo]
f_diff[1:1] = solveset(diff(f), x, Reals).evalf(2)

incr_list = []
decr_list = []

for i in range(1, len(f_diff)):
    val = is_increasing(f, Interval.open(f_diff[i - 1], f_diff[i]))
    if val:
        incr_list.append(f"[{f_diff[i - 1]}, {f_diff[i]}]")
    else:
        decr_list.append(f"[{f_diff[i - 1]}, {f_diff[i]}]")

print(f"убывает:", *decr_list, sep="\n")
print(f"Возростает:", *incr_list, sep="\n")


#построить график
plot(f, (x, -1, 1), legend=True)


#Вычеслить вершины - Экстремумы функции

from random import uniform

f_diff = sorted(solveset(diff(f),x, Reals).evalf(2))
f_diff.insert(0, f_diff[0]-1)
f_1 = diff(f)

ext_list = []

for i, val in enumerate(f_diff):
    ext_list.append(f_1.subs(x, uniform(val, f_diff[i]+1)))
    if i !=0:    
        if ext_list[i-1] < 0 < ext_list[i]:
            print(f"Точка минимума: {val}, {f.subs(x,val).evalf(2)}")
            
        elif ext_list[i-1] > 0 > ext_list[i]:
            print(f"Точка максимума: {val}, {f.subs(x,val).evalf(2)}")

# Определить промежутки , на которых f > 0
# Определить промежутки , на которых f < 0
# Промежутки знакопостоянства
 
print("f > 0:", end="")
solveset(f > 0 , x, Reals).evalf(2)

print("f < 0:", end="")
solveset(f < 0 , x, Reals).evalf(2)

