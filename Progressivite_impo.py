from openfisca_france import FranceTaxBenefitSystem
import matplotlib.pylab as plt
import numpy as np
import pandas as pd


#Create a df to store my alloc
salaire_de_base=np.linspace(0,100000,100)
print(salaire_de_base)

# Create a new scenario from openfisca_france
tax_benefit_system = FranceTaxBenefitSystem()
scenario = tax_benefit_system.new_scenario()

scenario.init_single_entity(

    # Axe declaration
    axes=[
        dict(  # in a dictionary
            count=100,  # 'count' : indicates the number of step
            min=0,
            max=100000,
            name='salaire_de_base',  # the variable you want to make evolve
        ),
    ],

    period=2014,
    parent1=dict(
        date_naissance='1980-01-01',
    )
)

simulation = scenario.new_simulation()

#Add variable related to irpp
income_tax = - simulation.calculate('irpp', 2014)
gross_wage = simulation.calculate_add('salaire_de_base', 2014)
taxable_income = simulation.calculate_add('salaire_imposable', 2014)

