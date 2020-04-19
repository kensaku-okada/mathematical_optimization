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

# 新しい数理最適化 p8

# +
from gurobipy import *

model = Model("lo1")
x1 = model.addVar(vtype="C", name="x1")
x2 = model.addVar(vtype="C", name="x2")
x3 = model.addVar(vtype="C", ub=30, name="x3")

model.update()

model.addConstr(2 * x1 + x2 + x3 <= 60)
model.addConstr(x1 + 2 * x2 + x3 <= 60)
model.setObjective(15 * x1 + 18 * x2 + 30 * x3, GRB.MAXIMIZE)

model.optimize()
print("--------------------")
print(f"Opt. Value= {model.ObjVal}")
    
for v in model.getVars():
    print(f"v.VarName= {v.VarName}, v.X= {v.X}")
      
      
      
# -


