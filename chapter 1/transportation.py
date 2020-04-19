# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# 新しい数理最適化 p12

# +
from gurobipy import *

# define data
# customer demand
d = {1:80, 2:270, 3:250, 4:160, 5:180}
# customer numbers
I = [1,2,3,4,5]
# capacity of each factory
M = {1:500, 2:500, 3:500}
# factory numbers
J = [1,2,3]

# transportation cost between customers and factories
c = {(1,1):4,    (1,2):6,    (1,3):9, 
     (2,1):5,    (2,2):4,    (2,3):7,
     (3,1):6,    (3,2):3,    (3,3):4,
     (4,1):8,    (4,2):5,    (4,3):3,
     (5,1):10,   (5,2):8,    (5,3):4,
     }

model = Model("transportation")

x = {}
for i in I:
    for j in J:
        x[i, j] = model.addVar(vtype="C", name="x(%s, %s)" % (i, j))

model.update()

print(f"x: {x}")

# add constraints
# constraint for satisfying customer demands 
for i in I:
    model.addConstr(quicksum(x[i, j] for j in J) == d[i], name = "Demand(%s)" % i)

# constraint for factory capacities
for j in J:
    model.addConstr(quicksum(x[i, j] for i in I) <= M[j], name = "Capacity(%s)" % j)

# objective function
model.setObjective(quicksum(c[i, j] * x[i , j] for (i, j) in x), GRB.MINIMIZE)
    
model.optimize()

print(f"optimal value: {model.ObjVal}")
EPS = 1.e-6
for (i, j) in x:
    if x[i, j].X > EPS:
        print(f"x[i, j]: {x[i, j]}, j: {j}, i: {i}")

print("-------------------")    
for (i, j) in x:
    print(f"x[i, j]: {x[i, j]}, j: {j}, i: {i}")
    

# -


