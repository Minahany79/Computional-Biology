from cobra import Model, Reaction, Metabolite


model = Model('task 1')

v1 = Reaction('v1')
v1.name = 'V1'

v2 = Reaction('v2')
v2.name = 'V2'

In = Reaction('In')
In.name = 'In'
In.lower_bound = 15
In.upper_bound = 15

Out = Reaction('Out')
Out.name = 'Out'

v3 = Reaction('v3')
v3.name = 'v3'
v3.lower_bound = 12
v3.upper_bound = 12

v4 = Reaction('v4')
v4.name = 'v4'

A = Metabolite(
    'A', compartment='c')
B = Metabolite(
    'B', compartment='c')
C = Metabolite(
    'C', compartment='c')
ATP = Metabolite(
    'ATP', compartment='c')


v1.add_metabolites({A: -1, B: 1})

v2.add_metabolites({B: -1, C: 1})

In.add_metabolites({A: 1})

Out.add_metabolites({C: -1})

v3.add_metabolites({A: -1, ATP: 1})

v4.add_metabolites({ATP: -1})

model.add_reactions([In, v1, v2, v3, v4, Out])

model.objective = Out
model.optimize()
model.summary()
