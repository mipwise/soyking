from soyking import input_schema
from soyking import output_schema

import pulp
import pandas as pd


def solve(dat):
    # Prepare optimization parameters
    sc = dat.shipping_costs
    I = list(dat.supplies['Farm ID'])
    J = list(dat.demands['DC ID'])
    av = dict(zip(dat.supplies['Farm ID'], dat.supplies['Availability']))
    dm = dict(zip(dat.demands['DC ID'],dat.demands['Demand']))
    costs = dict(zip(zip(sc['Farm ID'], sc['DC ID']), sc['Cost per ton']))
    x_keys = [(i, j) for i in I for j in J]

    # Build optimization model
    mdl = pulp.LpProblem("soyking", sense=pulp.LpMinimize)
    x = pulp.LpVariable.dicts(indexs=x_keys, cat=pulp.LpContinuous, lowBound=0.0, name='x')
    # Constraints
    for i in I:
        mdl.addConstraint(sum(x.get((i, j), 0) for j in J) <= av[i], name=f'av_{i}')
    for j in J:
        mdl.addConstraint(sum(x.get((i, j), 0) for i in I) >= dm[j], name=f'dm_{j}')


    # Objective function
    mdl.setObjective(sum(costs[i, j] * x[i, j] for i, j in x_keys))

    # Optimize and retrieve the solution
    mdl.solve()
    status = pulp.LpStatus[mdl.status]
    if status == 'Optimal':
        x_sol = [(i, j, var.value()) for (i, j), var in x.items()]
    else:
        x_sol = None
        print(f'Model is not optimal. Status: {status}')

    # Populate output schema
    sln = output_schema.PanDat()
    if x_sol:
        ship_flow_df = pd.DataFrame(x_sol, columns=['Farm ID', 'DC ID', 'Shipped tons'])
        # populate ship_flow table
        ship_flow_df = ship_flow_df.round({'Cost per ton': 2})
        ship_flow_df = ship_flow_df.astype({'Farm ID': str, 'DC ID': str, 'Shipped tons': 'Float64'})
        sln.ship_flow = ship_flow_df[['Farm ID', 'DC ID', 'Shipped tons']]
    return sln


