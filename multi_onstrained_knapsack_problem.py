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

# 新しい数理最適化 p29

# +
from gurobipy import *

def get_data():
#     item numbers and prices
    J,v = multidict({1:16, 2:19, 3:23, 4:28})
    
#     knapsack capacities: 7 = max weight, 10000 = max volume 
    I,b = multidict({1:7, 2:10000})
    
#     weight and volume of each item
    a = {(1,1):2,    (1,2):3,    (1,3):4,    (1,4):5,
         (2,1):3000, (2,2):3500, (2,3):5100, (2,4):7200,
         }

    return I,J,v,a,b

def mkp(I,J,v,a,b):
    model = Model("mkp")
    x = {}
#     define variablex
    for j in J:
        x[j] = model.addVar(vtype= "B", name="x[%d]" % j)
    model.update()
#     define constraints
    for i in I:
        model.addConstr(quicksum(a[i, j] * x[j] for j in J) <= b[i])
#     define objective function
    model.setObjective(quicksum(v[j] * x[j] for j in J), GRB.MAXIMIZE)
    return model
        
if __name__ == "__main__":
    I,J,v,a,b = get_data()
    model = mkp(I,J,v,a,b)
    
    model.update()
    model.write("mkp.lp")
    
    model.optimize()
    status = model.Status
    if status == GRB.status.OPTIMAL:
        print("the optimization status is optimal")
    elif status == GRB.status.INFEASIBLE:
        print("the optimization status is infeasible")
    
#     show result
    print(f"optimum value: {model.ObjVal}")
    for v in model.getVars():
        if v.X > 0.0:
            print(f"v.varName: {v.varName}. v.X: {v.X}")

# -


